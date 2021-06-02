package edu.ncsu.mos.semantics;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
import com.github.javaparser.ast.body.TypeDeclaration;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.hyperparameters.ConstructorExpansion;
import edu.ncsu.config.hyperparameters.HyperParameters;
import edu.ncsu.executors.ExecutionResult;
import edu.ncsu.executors.ExecutionUtils;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.executors.helpers.ReflectionHelper;
import edu.ncsu.executors.models.Function;
import edu.ncsu.executors.models.FunctionVariable;
import edu.ncsu.mos.store.ExecStore;
import edu.ncsu.mos.store.MetaStore;
import edu.ncsu.segmentation.SegmentUtils;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.helpers.VisitorHelper;
import org.apache.commons.lang3.StringUtils;

import java.lang.reflect.Method;
import java.util.*;
import java.util.logging.Logger;

class ExecutorAdapter extends VoidVisitorAdapter {
    private CompilationUnit compilationUnit;

    private String filePath;

    private String packageName;

    private Map<String, MethodDeclaration> functionASTs = new HashMap<>();

    public ExecutorAdapter(String filePath) {
        this.filePath = filePath;
        String contents = Utils.readFromFile(filePath);
        compilationUnit = VisitorHelper.parseContent(contents);
        packageName = VisitorHelper.getPackage(compilationUnit);
        for (TypeDeclaration typeDeclaration: compilationUnit.getTypes())
            parse(typeDeclaration);
    }

    private void parse(TypeDeclaration typeDeclaration) {
        if (!(typeDeclaration instanceof ClassOrInterfaceDeclaration))
            return;
        ClassOrInterfaceDeclaration classOrInterfaceDeclaration = (ClassOrInterfaceDeclaration) typeDeclaration;
        if (classOrInterfaceDeclaration.isInterface() || classOrInterfaceDeclaration.isAbstract())
            return;
        String typeName = classOrInterfaceDeclaration.getNameAsString();
        for (Object member: classOrInterfaceDeclaration.getMembers()) {
            if (member instanceof MethodDeclaration) {
                this.visit((MethodDeclaration) member, typeName);
            } else if (member instanceof TypeDeclaration) {
                this.parse((TypeDeclaration) member);
            }
        }
    }

    public void visit(MethodDeclaration methodDeclaration, Object parentClassName) {
        if (!methodDeclaration.getBody().isPresent() || methodDeclaration.isAbstract())
            return;
        String className = parentClassName.toString();
        String functionName = methodDeclaration.getNameAsString();
        List<String> argTypes = new ArrayList<>();
        if (!methodDeclaration.isStatic())
            return;
        String returnType = methodDeclaration.getType().getElementType().asString();
        if (returnType.equals("void"))
            return;
        if (methodDeclaration.getParameters() == null || methodDeclaration.getParameters().size() == 0)
            return;
        for (Parameter parameter: methodDeclaration.getParameters())
            argTypes.add(parameter.getType().getElementType().toString());
        String argTypeString = StringUtils.join(argTypes, ",");
        String key = String.format("%s.%s(%s)->%s", className, functionName, argTypeString, returnType);
        functionASTs.put(key, methodDeclaration);
    }

    public String getFilePath() {
        return filePath;
    }

    public Map<String, MethodDeclaration> getFunctionASTs() {
        return functionASTs;
    }

    public Set<String> getFunctionKeys() {
        return functionASTs.keySet();
    }

    public String getPackageName() {
        return packageName;
    }
}

public class MethodExecutors {

    private final static Logger LOGGER = Logger.getLogger(MethodExecutors.class.getName());


    private ExecutorAdapter adapter;

    private final static ExecStore EXEC_STORE = new ExecStore();

    private final static MetaStore META_STORE = new MetaStore();

    public MethodExecutors(String filePath) {
        adapter = new ExecutorAdapter(filePath);
    }

    private String makeCodeBlockKey(Method method, String className) {
        String methodName = method.getName();
        String returnType = ReflectionHelper.getBaseClass(method.getReturnType()).getName();
        List<String> argTypes = new ArrayList<>();
        java.lang.reflect.Parameter[] parameters = method.getParameters();
        if (parameters != null && parameters.length > 0) {
            for (java.lang.reflect.Parameter parameter: parameters) {
                argTypes.add(ReflectionHelper.getBaseClass(parameter.getType()).getName());
            }
        }
        String argTypeString = StringUtils.join(argTypes, ",");
        return String.format("%s.%s(%s)->%s", className, methodName, argTypeString, returnType);
    }

    @SuppressWarnings("rawtypes")
    private Map<String, Method> getMethods(Class clazz) {
        Map<String, Method> methods = new HashMap<>();
        for (Method method: clazz.getMethods()) {
            String key = makeCodeBlockKey(method, clazz.getSimpleName());
            if (adapter.getFunctionKeys().contains(key))
                methods.put(key, method);
        }
        return methods;
    }

    private static boolean hasTooManyArguments(List<FunctionVariable> arguments) {
        int argCount = 0;
        for (FunctionVariable argument : arguments)
            argCount += argument.getSystemClassConstructor() != null ? argument.getSystemClassConstructor().getTotalArguments() : 0;
//        return argCount > HyperParameters.MAX_NUM_ARGS;
        return argCount > 3;
    }

    public List<Function> permutateFunction(Function baseFunction, String key) {
        List<Function> functions = new ArrayList<>();
        if (baseFunction.getArguments().size() == 0) {
            LOGGER.severe(String.format("@COSAL: Method '%s' has no arguments!", baseFunction.getName()));
            return null;
        }
        if (baseFunction.getArguments().size() > 3) {
            LOGGER.severe(String.format("@COSAL: Method '%s' has too many arguments!", baseFunction.getName()));
            return null;
        }

        List<List<FunctionVariable>> argsPermutation = SegmentUtils.expandFunctionVariables(baseFunction, ConstructorExpansion.OPTIMAL);
        if (argsPermutation == null)
            throw new RuntimeException("@COSAL: Failed to create permutation. Check the function");
        for (List<FunctionVariable> args: argsPermutation) {
            JsonArray argsMetadata = new JsonArray();
            for (FunctionVariable arg: args)
                argsMetadata.add(arg.getMetadataAsJson());
            for (Map<String, List<String>> argPermutation: SegmentUtils.makePermutations(args)) {
                Function function = baseFunction.clone();
                function.setUuid(Utils.randomString());
                JsonObject metadata = new JsonObject();
                metadata.addProperty("name", function.getName());
                metadata.addProperty("project", ProjectConfig.PROJECT_NAME);
                metadata.addProperty("originalFunctionName", key);
                metadata.addProperty("body", baseFunction.getAst().toString());
                metadata.addProperty("filePath", adapter.getFilePath());
                metadata.addProperty("inputKey", Function.makeArgumentsKey(argPermutation));
                metadata.add("argsMetadata", argsMetadata);
                metadata.add("argsPermutation", Function.encodeArgsPermutation(argPermutation));
                metadata.add("returnMetadata", function.getReturnMetadata());
                function.setMetadata(metadata);
                functions.add(function);
            }
        }
        return functions;
    }

    @SuppressWarnings("rawtypes")
    public Map<String, List<Function>> getFunctions() {
        List<Class> classes = PackageManager.getClassesFromPackage(adapter.getPackageName());
        Map<String, List<Function>> functionsMap = new HashMap<>();
        for (Class clazz: classes) {
            for (Method method: clazz.getMethods()) {
                String key = makeCodeBlockKey(method, clazz.getSimpleName());
                if (!adapter.getFunctionKeys().contains(key))
                    continue;
                Function function = new Function(ProjectConfig.DATASET, method,
                        adapter.getFunctionASTs().get(key), adapter.getFilePath());
                List<Function> permutated = permutateFunction(function, key);
                if (permutated == null || permutated.size() == 0)
                    continue;
                functionsMap.put(key, permutated);
            }
        }
        return functionsMap;
    }

    public static void processJavaFile(String filePath, int fileIndex, int nFiles) {
        if (META_STORE.isFileProcessed(filePath)) {
//            LOGGER.info(String.format("Already processed file '%s'. Moving on!", filePath));
            return;
        }
        MethodExecutors executors = new MethodExecutors(filePath);
        if (executors.adapter.getFunctionKeys().size() == 0) {
//            LOGGER.info("No processable functions!");
            return;
        }
        LOGGER.info(String.format("Processing java file: %d / %d ... ", fileIndex + 1, nFiles));
        Map<String, List<Function>> functionsMap = executors.getFunctions();
        int totalFunctions = 0;
        for (List<Function> functions: functionsMap.values())
            totalFunctions += functions.size();
        LOGGER.info(String.format("Need to execute '%d' functions ... ", totalFunctions));
        int index = 0;
        for (String key: functionsMap.keySet()) {
            EXEC_STORE.deleteClassFunctionMetadata(filePath, key);
            EXEC_STORE.deleteClassFunctionResult(filePath, key);
            LOGGER.info(String.format("Processing '%d' functions for key '%s' ... ", functionsMap.get(key).size(), key));
            List<Function> functions = functionsMap.get(key);
            functions.parallelStream().forEach(MethodExecutors::executeFunction);
            index += functions.size();
        }
        META_STORE.updateFileProcessed(filePath);
        ExecutionUtils.shutdownExecutor();
    }


    public static void executeFunction(Function function) {
        try {
            // 1. Load Arguments
            List<Object[]> arguments = ExecutionUtils.loadArguments(function, HyperParameters.FUZZ_ARGUMENT_SIZE);
            if (arguments == null || arguments.size() == 0)
                throw new RuntimeException(String.format("@COSAL: Unable to generate arguments for the function: %s", function.getName()));
            // 2. Execute functions
            List<ExecutionResult> executionResults;
            try {
                executionResults = ExecutionUtils.executeFunction(function, arguments);
                if (executionResults == null || executionResults.size() == 0)
                    throw new RuntimeException(String.format("Exception while executing function: %s", function.getName()));
            } catch (Exception e) {
                throw new RuntimeException(String.format("Exception while executing function: %s", function.getName()));
            }
            JsonObject executedFunction = ExecutionUtils.executeFunctionAsJSON(function, arguments);
            executedFunction.addProperty("originalFunctionName", function.getMetadata().get("originalFunctionName").getAsString());
            executedFunction.addProperty("filePath", function.getMetadata().get("filePath").getAsString());
            // 3. Save function metadata
            EXEC_STORE.saveClassFunctionMetadata(function.getMetadata());
            // 4. Save function result
            if (executedFunction.has("outputs")) {
                LOGGER.info(String.format("Saved function results of '%s' in table 'functions_executed'", function.getName()));
                EXEC_STORE.updateFunctionResult(executedFunction);
            } else if (executedFunction.has("errorTrace")) {
                LOGGER.info(String.format("Saved function error of '%s' in table 'functions_failed'", function.getName()));
                EXEC_STORE.updateFunctionError(executedFunction);
            }
        } catch (Exception e) {
            LOGGER.severe("Encountered error while saving. Continuing though ... ");
            e.printStackTrace();
        }

    }


    public static void getJavaFiles() {
        String[] folders = Utils.listDir(ProjectConfig.PROJECTS_JAVA_FOLDER);
        int folderIndex = 0;

        for (String folder: folders) {
            String folderPath = Utils.pathJoin(ProjectConfig.PROJECTS_JAVA_FOLDER, folder);
            int fileIndex = 0;
            List<String> javaFiles = Utils.listNonGeneratedJavaFiles(folderPath);
            LOGGER.info(String.format("Processing folder %d/%d. # files = %d ... ", folderIndex + 1, folders.length, javaFiles.size()));
            for(String javaFile: javaFiles) {
                processJavaFile(javaFile, fileIndex, javaFiles.size());
                fileIndex += 1;
            }
            folderIndex += 1;
        }
    }

    public static void main(String[] args) {
        getJavaFiles();
//        processJavaFile("/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/atcoder/src/main/java/C73/P0/S1577233/Main.java");
//        getJavaFiles();
    }

}
