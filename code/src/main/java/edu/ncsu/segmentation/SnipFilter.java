package edu.ncsu.segmentation;

import com.github.javaparser.ast.NodeList;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
import com.github.javaparser.ast.body.VariableDeclarator;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.stmt.ReturnStmt;
import com.github.javaparser.ast.stmt.Statement;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import edu.ncsu.arguments.ArgumentGenerator;
import edu.ncsu.arguments.ObjectTypeArguments;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.config.hyperparameters.ConstructorExpansion;
import edu.ncsu.config.hyperparameters.HyperParameters;
import edu.ncsu.executors.ExecutionResult;
import edu.ncsu.executors.ExecutionUtils;
import edu.ncsu.executors.MethodExecutor;
import edu.ncsu.executors.helpers.FileHandler;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.executors.models.Function;
import edu.ncsu.executors.models.FunctionVariable;
import edu.ncsu.executors.models.Primitive;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.utils.MavenUtils;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.logging.Logger;

public class SnipFilter {

    private static final Logger LOGGER = Logger.getLogger(SnipFilter.class.getName());

    private String dataset;

    private ClassMethods classMethods;

    private IMetadataStore metadataStore;

    public ClassMethods getClassMethods() {
        return classMethods;
    }

    private static final boolean DEBUG = true;

    public SnipFilter(String dataset, String generatedFile) {
        this.dataset = dataset;
        this.classMethods = new ClassMethods(this.dataset, generatedFile);
        this.metadataStore = BaseStorage.loadMetadataStore(this.dataset);
    }

    public SnipFilter(String generatedFile) {
        this(ProjectConfig.DATASET, generatedFile);
    }

    private boolean isValidParameterTypes(Function function) {
        for (FunctionVariable param : function.getArguments()) {
            if (param.getPrimitive() != null)
                continue;
            if (FileHandler.isInputClass(param.getFullTypeKey()))
                continue;
            if (!ObjectTypeArguments.isValidClass(param.getFullTypeKey()))
                return false;
        }
        return true;
    }

    private boolean isVariableModified(Function function, String variableName) {
        FunctionVariable retVariable = function.getReturnVariable();
        SnipFilterVisitor visitor = new SnipFilterVisitor(function, variableName);
        visitor.traverse();
        if (retVariable.getPrimitive() != null && retVariable.getArrayDimensions() == 0) {
            return visitor.getVariableUpdated();
        } else {
//            return visitor.getVariableTouched();
            return checkFunctionValidityViaFuzzing(function);
        }

    }

    private boolean checkFunctionValidityViaFuzzing(Function function) {
        // 1. Assign most optimal constructor for function variables - Done
        boolean isValid = setMetadataForFunctionVariables(function);
        if (! isValid)
            return false;
        // 2. Generate random arguments - Done
        List<Object[]> arguments = ExecutionUtils.loadArguments(function, HyperParameters.DYNAMIC_VALIDATION_ARGUMENT_SIZE);
        if (arguments == null || arguments.size() == 0)
            return false;
        // 3. Execute functions - Done
        List<ExecutionResult> executionResults;
        try {
            executionResults = ExecutionUtils.executeFunction(function, arguments);
            if (executionResults == null || executionResults.size() == 0)
                return false;
        } catch (Exception e) {
            LOGGER.severe(String.format("Exception while executing function: %s", function.getName()));
            e.printStackTrace();
            return false;
        }
        // 4. Check if function changes - Inprogress
        List<Object[]> clonedArguments = ExecutionUtils.loadArguments(function, HyperParameters.DYNAMIC_VALIDATION_ARGUMENT_SIZE);
        return checkOutputValidity(executionResults, clonedArguments);
    }

    private boolean setMetadataForFunctionVariables(Function function) {
        List<List<FunctionVariable>> argsPermutation = SegmentUtils.expandFunctionVariables(function, ConstructorExpansion.OPTIMAL);
        if (argsPermutation == null)
            return false;
        function.setArguments(argsPermutation.get(0));
        JsonArray argsMetadata = new JsonArray();
        for (FunctionVariable arg: function.getArguments()) {
            argsMetadata.add(arg.getMetadataAsJson());
        }
        JsonObject metadata = function.getMetadata();
        Map<String, List<String>> argPermutation = SegmentUtils.makePermutations(function.getArguments()).get(0);
        metadata.addProperty("inputKey", Function.makeArgumentsKey(argPermutation));
        metadata.add("argsMetadata", argsMetadata);
        metadata.add("argsPermutation", Function.encodeArgsPermutation(argPermutation));
        function.setMetadata(metadata);
        return true;
    }

    private boolean checkOutputValidity(List<ExecutionResult> executionResults, List<Object[]> arguments) {
        assert executionResults.size() == arguments.size(); // Ensure that there are same number of inputs and outputs
        List<Boolean> argMatches = new ArrayList<>();
        boolean previousResultMatch = true;
        for (int argIndex = 0; argIndex < arguments.get(0).length; argIndex ++)
            argMatches.add(true);
        for (int resultIndex=0; resultIndex < arguments.size(); resultIndex++) {
            Object returnValue = executionResults.get(resultIndex).getContent();
            if (resultIndex > 0 && previousResultMatch)
                previousResultMatch = ObjectTypeArguments.areSameObjects(returnValue, executionResults.get(resultIndex - 1).getContent());
            boolean isAnyTrue = argMatches.stream().anyMatch(argMatch -> argMatch);
            if (isAnyTrue) {
                // Return Value matches with atleast one of the arguments in any of the previous values
                for (int argIndex = 0; argIndex < arguments.get(resultIndex).length; argIndex++) {
                    if (!argMatches.get(argIndex)) // Argument does not match with returnValue in one of the previous cases
                        continue;
                    Object argument = arguments.get(resultIndex)[argIndex];
                    argMatches.set(argIndex, ObjectTypeArguments.areSameObjects(returnValue, argument));
                }
            }
            isAnyTrue = argMatches.stream().anyMatch(argMatch -> argMatch);
            if (!isAnyTrue && !previousResultMatch)
                return true;
        }
        return false;
    }


    private boolean isReturnVariableModified(Function function) {
        MethodDeclaration ast = this.classMethods.getMethodBody(function.getName());
        if (!ast.getBody().isPresent())
            return false;
        NodeList<Statement> statements = ast.getBody().get().getStatements();
        Statement lastStmt = statements.get(statements.size() - 1);
        if (!(lastStmt instanceof ReturnStmt))
            return checkFunctionValidityViaFuzzing(function);
        ReturnStmt returnStmt = (ReturnStmt) lastStmt;
        if (!returnStmt.getExpression().isPresent())
            return false;
        Expression expression = returnStmt.getExpression().get();
        if (!(expression instanceof NameExpr))
            // Implies that it is returning an operation of a call
            return true;
        String returnVariableName =  ((NameExpr) expression).getNameAsString();
        return isVariableModified(function, returnVariableName);
    }

    private boolean hasTooManyArguments(Function function) {
        int argsCount = 0;
        if (function.getArguments().size() > HyperParameters.MAX_NUM_ARGS)
            return true;
        for (FunctionVariable argument: function.getArguments()) {
            String argKey = argument.getFullTypeKey();
            if (argument.getPrimitive() != null) {
                argsCount += 1;
            } else if (FileHandler.isInputOutputClass(argKey)) {
                argsCount += 1;
            } else if (ObjectTypeArguments.isValidClass(argKey)) {
                int objArgsCount = ObjectTypeArguments.getSimplestConstructorArgsCount(argKey);
                if (objArgsCount == -1)
                    return false;
                argsCount += objArgsCount;
            }
        }
        return argsCount > HyperParameters.MAX_NUM_ARGS;
//        return function.getArguments() != null && function.getArguments().size() > HyperParameters.MAX_NUM_ARGS;
    }

    public boolean isValidFunction(Function function) {
//        if (!function.isFuzzable())
//            return true;
        if (Primitive.isVoid(function.getReturnVariable().getFullTypeKey())) {
            return false;
        } else if (FileHandler.isInputClass(function.getReturnVariable().getFullTypeKey())) {
            return false;
        } else if (hasTooManyArguments(function)) {
            return false;
        } else if (!isValidParameterTypes(function)) {
            return false;
        } else {
            try {
                return isReturnVariableModified(function);
            } catch (Exception e) {
                LOGGER.severe(String.format("Exception while executing function: %s", e.getMessage()));
                e.printStackTrace();
                return false;
            }
        }
    }

    public static void filterFile(String generatedFile) {
        String fileName = Utils.getFileName(generatedFile);
        if (!fileName.startsWith(Settings.GENERATED_CLASS_PREFIX)) {
            LOGGER.info(String.format("'%s' is not a generated file. Not permutating!", Utils.getRepoLocalPath(generatedFile)));
            return;
        }
        SnipFilter snipFilter = new SnipFilter(generatedFile);
        List<Function> validFunctions = new ArrayList<>();
        List<String> functionsToDelete = new ArrayList<>();
        Map<String, Method> methods = snipFilter.getClassMethods().getMethods();
        Map<String, Function> processedFunctions = snipFilter.getClassMethods().getFilteredFunctions();
        if (methods.size() == processedFunctions.size()) {
            LOGGER.info(String.format("\nProcessed file '%s' with '%d' methods ... ", Utils.getRepoLocalPath(generatedFile), methods.size()));
            return;
        }
        LOGGER.info(String.format("\nProcessing file '%s' with '%d' methods ... ", Utils.getRepoLocalPath(generatedFile), methods.size()));
        methods.forEach(
                (methodName, method) -> {
//                    if (!methodName.equals("func_9efee1be704845b3a3a3bb8ef3e68210"))
//                        return;
                    if (DEBUG)
                        LOGGER.info(String.format("Checking validity of function '%s' ... ", methodName));
                    Function function = snipFilter.getClassMethods().getFunction(methodName);
                    if (function == null) {
                        functionsToDelete.add(methodName);
                        return;
                    }
                    if (function.getMetadata().has("isFiltered")) {
//                        if (DEBUG)
//                            LOGGER.info(String.format("'%s' is already processed and VALID!", methodName));
                        validFunctions.add(function);
                        return;
                    }
                    if (snipFilter.isValidFunction(function)) {
//                        if (DEBUG)
//                            LOGGER.info(String.format("'%s' is VALID!", methodName));
                        validFunctions.add(function);
                    } else {
//                        if (DEBUG)
//                            LOGGER.info(String.format("'%s' is INVALID!", methodName));
                        functionsToDelete.add(methodName);
                    }
                }
        );
        SegmentUtils.writeFunctionsToFile(validFunctions, snipFilter.getClassMethods().getPackageName(), snipFilter.getClassMethods().getClassName(), generatedFile);
        validFunctions.forEach((function -> {
            snipFilter.metadataStore.updateFunctionMetadata(function.getName(), "isFiltered", true);
        }));
        snipFilter.metadataStore.deleteClassFunctionsMetadata(functionsToDelete);
        LOGGER.info(String.format("Reduced '%d' functions to '%d' functions after filtering!", snipFilter.getClassMethods().getMethods().size(), validFunctions.size()));
        ExecutionUtils.shutdownExecutor();
    }

    public static void main(String[] args) {
//        filterFile("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/Y11R5P1/Egor/generated_class_e1e3e0f1ce744abe828ec2d08805fc8c.java");
        LOGGER.info(String.format("Filtering generated files for dataset: '%s'", ProjectConfig.DATASET));
        MavenUtils.buildProject();
        filterFile("/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/guava/src/com/google/common/base/generated_class_dea663fe58114b6ab0dba2a28dc6f942.java");
        MavenUtils.buildProject();
    }

}

@SuppressWarnings("rawtypes")
class SnipFilterVisitor extends VoidVisitorAdapter {

    private Function function;

    private String returnVariableName;

    private Boolean isVariableCreated = false;

    private Boolean isVariableUpdated = false;

    private Boolean isVariableTouched = false;

    public Boolean getVariableUpdated() {
        return isVariableUpdated;
    }

    public Boolean getVariableTouched() {
        return isVariableTouched;
    }

    public SnipFilterVisitor(Function function, String returnVariableName) {
        this.function = function;
        this.returnVariableName = returnVariableName;
    }

    public void traverse() {
        this.visit(this.function.getAst(), null);
    }

    @SuppressWarnings("unchecked")
    @Override
    public void visit(MethodDeclaration methodDeclaration, Object arg) {
        methodDeclaration.getParameters().forEach(p -> p.accept(this, arg));
        methodDeclaration.getBody().ifPresent(l -> l.accept(this, arg));
    }

    @Override
    public void visit(Parameter methodParameter, Object arg) {
        String parameterName = methodParameter.getNameAsString();
        if (parameterName.equals(this.returnVariableName))
            isVariableCreated = true;
    }

    @Override
    public void visit(VariableDeclarationExpr variableDeclaratorExpr, Object arg) {
        for (VariableDeclarator variableDeclarator: variableDeclaratorExpr.getVariables()) {
            String variableName = variableDeclarator.getNameAsString();
            if (variableName.equals(this.returnVariableName)) {
                isVariableCreated = true;
                if (variableDeclarator.getInitializer().isPresent()) {
                    isVariableUpdated = true;
                }
            }
            if (variableDeclarator.getInitializer().isPresent()) {
                VisitorHelper.visit(this, variableDeclarator.getInitializer().get(), arg);
            }
        }
    }

    @Override
    public void visit(AssignExpr assignExpr, Object arg) {
        if (assignExpr.getTarget() instanceof NameExpr) {
            NameExpr n = (NameExpr) assignExpr.getTarget();
            String variableName = n.getNameAsString();
            if (variableName.equals(returnVariableName)) {
                if (!isVariableCreated) {
                    throw new RuntimeException("@COSAL: Variable is UPDATED before created. Check business logic!!!");
                }
                isVariableUpdated = true;
            } else {
                VisitorHelper.visit(this, assignExpr.getValue(), arg);
            }
        } else {
            VisitorHelper.visit(this, assignExpr.getTarget(), arg);
            VisitorHelper.visit(this, assignExpr.getValue(), arg);
        }
    }

    @Override
    public void visit(UnaryExpr unaryExpr, Object arg) {
        if (unaryExpr.getExpression() instanceof NameExpr) {
            NameExpr n = (NameExpr) unaryExpr.getExpression();
            String variableName = n.getNameAsString();
            if (variableName.equals(returnVariableName)) {
                if (!isVariableCreated) {
                    throw new RuntimeException("@COSAL: Variable is UPDATED before created. Check business logic!!!");
                }
                isVariableUpdated = true;
                return;
            }
        }
        VisitorHelper.visit(this, unaryExpr.getExpression(), arg);
    }

    @Override
    public void visit(NameExpr nameExpr, Object arg) {
        String variableName = nameExpr.getNameAsString();
        if (variableName.equals(returnVariableName)) {
            if (!isVariableCreated) {
                throw new RuntimeException("@COSAL: Variable is TOUCHED before created. Check business logic!!!");
            }
            isVariableTouched = true;
        }
    }


}
