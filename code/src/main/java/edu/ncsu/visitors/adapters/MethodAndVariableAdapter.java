package edu.ncsu.visitors.adapters;

import com.github.javaparser.ParseResult;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.NodeList;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.stmt.ForEachStmt;
import com.github.javaparser.ast.stmt.ForStmt;
import com.github.javaparser.ast.stmt.WhileStmt;
import com.github.javaparser.ast.type.ClassOrInterfaceType;
import com.github.javaparser.ast.type.Type;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import com.google.common.collect.Sets;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import edu.ncsu.config.Settings;
import edu.ncsu.config.hyperparameters.HyperParameters;
import edu.ncsu.config.hyperparameters.SnipperMode;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.helpers.Constants;
import edu.ncsu.visitors.helpers.StatementHelper;

import edu.ncsu.visitors.blocks.*;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.io.*;
import java.util.*;
import java.util.logging.Logger;

public class MethodAndVariableAdapter extends VoidVisitorAdapter{

    private static final Logger LOGGER = Logger.getLogger(MethodAndVariableAdapter.class.getName());

    private static final Gson GSON = new GsonBuilder().create();

    private String dataset;

    private ParseResult<CompilationUnit> compilationUnitParseResult;

    private String fileName;

    private CommentAdapter commentAdapter;

    private List<ClassBlock> classBlocks;

    private Set<Integer> linesCovered;

    public String getDataset() {
        return this.dataset;
    }

    public String getFileName() {
        return this.fileName;
    }

    public CompilationUnit getCompilationUnit() {
        return VisitorHelper.loadCompilationUnit(compilationUnitParseResult);
    }

    public List<ClassBlock> getClassBlocks() {
        return this.classBlocks;
    }

    public MethodAndVariableAdapter(String dataset, String javaFile){
        this.dataset = dataset;
        this.linesCovered = new HashSet<>();
        this.fileName = javaFile;
        this.compilationUnitParseResult = VisitorHelper.parseFile(fileName);
        CompilationUnit compilationUnit = VisitorHelper.loadCompilationUnit(compilationUnitParseResult);
        this.commentAdapter = new CommentAdapter(fileName, compilationUnitParseResult);
        NodeList<TypeDeclaration<?>> types = compilationUnit.getTypes();
        String fileSource = compilationUnit.toString();
        this.classBlocks = new ArrayList<>();
        for (TypeDeclaration type: types) {
            classBlocks.add(parseTypeDeclaration(type, fileSource));
        }
    }

    private ClassBlock parseTypeDeclaration(TypeDeclaration typeDeclaration, String fileSource) {
        String className = typeDeclaration.getName().getIdentifier();
        Map<String, Variable> fieldVariablesMap = new HashMap<>();
        NodeList members = typeDeclaration.getMembers();
        List<MethodBlock> methodBlocks = new ArrayList<>();
        List<ClassBlock> innerClasses = new ArrayList<>();
        for (Object member: members) {
            if (member instanceof FieldDeclaration) {
                FieldDeclaration field = (FieldDeclaration) member;
                for (VariableDeclarator fieldVariable : field.getVariables()) {
                    Type fieldType = fieldVariable.getType();
                    String variableName = fieldVariable.getNameAsString();
                    Integer beginLine = null, beginColumn = null;
                    if (fieldVariable.getBegin().isPresent()) {
                        beginLine = fieldVariable.getBegin().get().line;
                        beginColumn = fieldVariable.getBegin().get().column;
                    }
                    Expression initValue = fieldVariable.getInitializer().isPresent() ? fieldVariable.getInitializer().get(): null;
                    fieldVariablesMap.put(variableName,
                            new Variable(variableName, fieldType,
                                    beginLine, beginColumn, initValue,
                                    typeDeclaration, field.getModifiers()));
                }
            } else if (member instanceof MethodDeclaration) {
                MethodDeclaration method = (MethodDeclaration) member;
                MethodBlock methodBlock = new MethodBlock(method, fileSource, className);
                methodBlocks.add(methodBlock);
            } else if (member instanceof ClassOrInterfaceDeclaration) {
                innerClasses.add(parseTypeDeclaration((ClassOrInterfaceDeclaration) member, fileSource));
            }
        }
        return new ClassBlock(typeDeclaration, compilationUnitParseResult, fileName, fieldVariablesMap, methodBlocks, innerClasses);
    }

    @SuppressWarnings("unchecked")
    @Override
    public void visit(MethodDeclaration methodDeclaration, Object arg) {
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        if (!methodDeclaration.getBody().isPresent())
            return;
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        MethodBlock methodBlock = (MethodBlock) visitorArg.get("method");
        List<Parameter> methodParameters = methodDeclaration.getParameters();
        for (Parameter methodParameter: methodParameters) {
            Type paramType = methodParameter.getType();
            if (paramType.getElementType() instanceof ClassOrInterfaceType) {
                visit((ClassOrInterfaceType) paramType.getElementType(), arg);
            }
            Integer beginLine = null, beginColumn = null;
            if (methodParameter.getBegin().isPresent()) {
                beginLine = methodParameter.getBegin().get().line;
                beginColumn = methodParameter.getBegin().get().column;
            }
            Variable parameter = new Variable(methodParameter.getName().asString(), paramType,
                    beginLine, beginColumn,
                    null, methodBlock.getMethodNode());
            if (methodParameter.isVarArgs())
                parameter.setArrayDimensions(parameter.getArrayDimensions() + 1);
            methodBlock.insertVariableDeclare(parameter);
        }
        visitorArg.put("method", methodBlock);
        if (methodDeclaration.getBody().isPresent())
            visit(methodDeclaration.getBody().get(), visitorArg);
    }

    @SuppressWarnings("unchecked")
    @Override
    public void visit(VariableDeclarationExpr variableDeclaratorExpr, Object arg) {
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        MethodBlock methodBlock = (MethodBlock) visitorArg.get("method");
        Type type = variableDeclaratorExpr.getCommonType();
        if (type.getElementType() instanceof ClassOrInterfaceType) {
            visit((ClassOrInterfaceType) type.getElementType(), arg);
        }
        for (VariableDeclarator variableDeclarator: variableDeclaratorExpr.getVariables()) {
            Type varType = variableDeclarator.getType();
            Integer beginLine = null, beginColumn = null;
            if (variableDeclarator.getBegin().isPresent()) {
                beginLine = variableDeclarator.getBegin().get().line;
                beginColumn = variableDeclarator.getBegin().get().column;
            }
            Expression initValue = variableDeclarator.getInitializer().isPresent() ? variableDeclarator.getInitializer().get(): null;
            Variable variable = new Variable(variableDeclarator.getNameAsString(),
                    varType, beginLine, beginColumn,
                    initValue, getParentNode(variableDeclarator));
            methodBlock.insertVariableDeclare(variable);
            methodBlock.insertVariableUsage(variable.getName(), variable.getStartPosition());
            variable.insertAssignPosition(variable.getStartPosition());
            if (initValue != null) {
                visit(variableDeclarator, arg);
            }
        }
    }

    @SuppressWarnings("unchecked")
    @Override
    public void visit(MethodCallExpr methodCallExpr, Object arg) {
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        if (!methodCallExpr.getScope().isPresent()) {
            Map<String, Object> visitorArg = (Map<String, Object>) arg;
            ClassBlock classBlock = (ClassBlock) visitorArg.get("class");
            if (classBlock.isStaticMethod(methodCallExpr.getNameAsString())) {
                methodCallExpr.setName(String.format("%s.%s", classBlock.getName(), methodCallExpr.getNameAsString()));
            }
        } else {
            Map<String, Object> visitorArg = (Map<String, Object>) arg;
            VisitorHelper.visit(this, methodCallExpr.getScope().get(), visitorArg);
        }
        if (methodCallExpr.getArguments() != null) {
            for (Expression param: methodCallExpr.getArguments())
                VisitorHelper.visit(this, param, arg);
        }
    }

    private Node getParentNode(VariableDeclarator variableDeclarator) {
        Optional<Node> parentNode = variableDeclarator.getParentNode();
        while (parentNode.isPresent()  && ! StatementHelper.BLOCK_NODE_NAMES.contains(parentNode.get().getClass().getName())) {
            parentNode = parentNode.get().getParentNode();
        }
        return parentNode.orElse(null);
    }

    @SuppressWarnings("unchecked")
    @Override
    public void visit(ForStmt forStmt, Object arg) {
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        forStmt.getInitialization().forEach(p -> p.accept(this, arg));
        forStmt.getCompare().ifPresent(l -> l.accept(this, arg));
        forStmt.getUpdate().forEach(p -> p.accept(this, arg));
        forStmt.getBody().accept(this, arg);
        forStmt.getComment().ifPresent(l -> l.accept(this, arg));
    }

    @SuppressWarnings("unchecked")
    @Override
    public void visit(ForEachStmt forEachStmt, Object arg) {
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        forEachStmt.getVariable().accept(this, arg);
        forEachStmt.getIterable().accept(this, arg);
        forEachStmt.getBody().accept(this, arg);
        forEachStmt.getComment().ifPresent(l -> l.accept(this, arg));
    }

    @SuppressWarnings("unchecked")
    @Override
    public void visit(WhileStmt whileStmt, Object arg) {
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        whileStmt.getCondition().accept(this, arg);
        whileStmt.getBody().accept(this, arg);
        whileStmt.getComment().ifPresent(l -> l.accept(this, arg));
    }

    @SuppressWarnings("unchecked")
    @Override
    public void visit(AssignExpr assignExpr, Object arg) {
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        MethodBlock methodBlock = (MethodBlock) visitorArg.get("method");
        ClassBlock classBlock = (ClassBlock) visitorArg.get("class");
        if (assignExpr.getTarget() instanceof NameExpr) {
            NameExpr n = (NameExpr) assignExpr.getTarget();
            updateStaticVariable(n, methodBlock, classBlock);
            Integer beginLine = null, beginColumn = null;
            if (n.getBegin().isPresent()) {
                beginLine = n.getBegin().get().line;
                beginColumn = n.getBegin().get().column;
            }
            VariablePosition position = new VariablePosition(beginLine, beginColumn);
            VisitorHelper.updateVariableUsage(n.getNameAsString(), position, methodBlock, classBlock, true);
        } else if (assignExpr.getTarget() instanceof FieldAccessExpr) {
            FieldAccessExpr t = (FieldAccessExpr) assignExpr.getTarget();
            if (t.getScope() != null && t.getScope() instanceof NameExpr &&
                    ((NameExpr) t.getScope()).getNameAsString().equals(classBlock.getName())) {
                Integer beginLine = null, beginColumn = null;
                if (t.getBegin().isPresent()) {
                    beginLine = t.getBegin().get().line;
                    beginColumn = t.getBegin().get().column;
                }
                VariablePosition position = new VariablePosition(beginLine, beginColumn);
                NameExpr n = t.getNameAsExpression();
                if (classBlock.getFieldVariables().containsKey(n.getNameAsString())) {
                    Variable fieldVariable = classBlock.getFieldVariables().get(n.getNameAsString());
                    fieldVariable.insertAssignPosition(position);
                    fieldVariable.insertUsedPosition(position);
                    classBlock.getFieldVariables().put(n.getNameAsString(), fieldVariable);
                }
            }
        }
        VisitorHelper.visit(this, assignExpr.getTarget(), visitorArg);
        VisitorHelper.visit(this, assignExpr.getValue(), visitorArg);
    }

    @Override
    public void visit(ArrayAccessExpr arrayAccessExpr, Object arg) {
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        VisitorHelper.visit(this, arrayAccessExpr.getName(), arg);
        VisitorHelper.visit(this, arrayAccessExpr.getIndex(), arg);
    }


    @SuppressWarnings("unchecked")
    @Override
    public void visit(NameExpr n, Object arg) {
//        super.visit(n, arg);
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        MethodBlock methodBlock = (MethodBlock) visitorArg.get("method");
        ClassBlock classBlock = (ClassBlock) visitorArg.get("class");
        updateStaticVariable(n, methodBlock, classBlock);
        Integer beginLine = null, beginColumn = null;
        if (n.getBegin().isPresent()) {
            beginLine = n.getBegin().get().line;
            beginColumn = n.getBegin().get().column;
        }
        VariablePosition position = new VariablePosition(beginLine, beginColumn);
        VisitorHelper.updateVariableUsage(n.getNameAsString(), position, methodBlock, classBlock, false);
    }

    @SuppressWarnings("unchecked")
    @Override
    public void visit(ClassOrInterfaceType type, Object arg) {
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        ClassBlock classBlock = (ClassBlock) visitorArg.get("class");
        if (!type.getScope().isPresent() && classBlock.containsInnerClass(type.getNameAsString())) {
            type.setName(String.format("%s.%s", classBlock.getName(), type.getName()));
        }
    }

    @SuppressWarnings("unchecked")
    @Override
    public void visit(ObjectCreationExpr objectCreationExpr, Object arg) {
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        ClassBlock classBlock = (ClassBlock) visitorArg.get("class");
        ClassOrInterfaceType type = objectCreationExpr.getType();
        if (type.getScope().isPresent() && classBlock.containsInnerClass(type.getNameAsString())) {
            type.setName(String.format("%s.%s", classBlock.getName(), type.getName()));
        }
        if (objectCreationExpr.getArguments() != null) {
            for (Expression expression: objectCreationExpr.getArguments()) {
                VisitorHelper.visit(this, expression, arg);
            }
        }
    }

    private void updateStaticVariable(NameExpr n, MethodBlock methodBlock, ClassBlock classBlock) {
        String variableName = n.getNameAsString();
        if (methodBlock.getVariableDeclareMap() == null || methodBlock.getVariableDeclareMap().containsKey(variableName))
            return;
        if (classBlock.getFieldVariables().containsKey(variableName)) {
            Variable variable = classBlock.getFieldVariables().get(variableName);
            Node parentNode = n.getParentNode().orElse(null);
            if (VisitorHelper.isStatic(variable.getModifiers()) && !(parentNode instanceof FieldAccessExpr)) {
                n.setName(String.format("%s.%s", classBlock.getName(), n.getName()));
            }
        }
    }


    private DummyMethod makeFunction(List<StatementBlock> statementBlocks, ClassBlock classBlock, MethodBlock methodBlock) {
        Map<String, Collection<Variable>> methodVariables = StatementHelper.getUndeclaredVariables(statementBlocks, classBlock, methodBlock);
        return new DummyMethod(dataset, classBlock, methodBlock, statementBlocks, methodVariables.get("undeclared"), methodVariables.get("declared"));
    }

    private Set<Integer> getLinesCovered(DummyMethod method) {
        Set<Integer> methodLineNumbers = method.getLineNumbers();
        return Sets.intersection(methodLineNumbers, commentAdapter.getSourceCodeLines());
    }

    @SuppressWarnings("unchecked")
    public String getMainClassName() {
        for (TypeDeclaration type: getCompilationUnit().getTypes()) {
            if (VisitorHelper.getScopeModifier(type.getModifiers()).equals(Constants.PUBLIC))
                return type.getNameAsString();
        }
        return null;
    }

    public void dumpSLOCStats(List<GeneratedFunction> generatedFunctions) {
        LOGGER.info("Dumping SLOC stats ... ");
        String packageName = VisitorHelper.getPackage(getCompilationUnit());
        String metaFolder = Utils.pathJoin(Settings.META_RESULTS_SLOC, packageName.replaceAll("\\.", File.separator));
        Utils.mkdir(metaFolder);
        File file = new File(Utils.pathJoin(metaFolder, "sloc.json"));
        Set<Integer> sloc = commentAdapter.getSourceCodeLines();
        Map<String, Map<String, Object>> slocMap;
        if (file.exists()) {
            try {
                Reader reader = new FileReader(file);
                slocMap = GSON.fromJson(reader, new TypeToken<Map<String, Map<String, Object>>>(){}.getType());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        } else {
            slocMap = new HashMap<>();
        }
        Map<String, Object> stats = new HashMap<>();
        stats.put("sloc", sloc);
        stats.put("linesCovered", linesCovered);
        stats.put("numFunctions", generatedFunctions.size());
        slocMap.put(fileName, stats);
        try(Writer writer = new FileWriter(file)) {
            Gson gson = new GsonBuilder().create();
            gson.toJson(slocMap, writer);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public List<GeneratedFunction> generateMethods() {
        LOGGER.info(String.format("PROCESSING FOR %s", this.fileName));
        List<GeneratedFunction> functions = new ArrayList<>();
        Set<String> existingFunctions  = new HashSet<>();
        for (ClassBlock classBlock: this.getClassBlocks()) {
            for (MethodBlock methodBlock: classBlock.getMethodBlocks()) {
//                LOGGER.info(String.format("*** %s.%s ***", classBlock.getName(), methodBlock.getName()));
                Map<String, Object> visitorArg = new HashMap<>();
                visitorArg.put("class", classBlock);
                visitorArg.put("method", methodBlock);
                this.visit(methodBlock.getMethodNode(), visitorArg);
                if (HyperParameters.SNIPPER_MODE == SnipperMode.METHOD) {
                    List<StatementBlock> statementBlocks = methodBlock.getStatements();
                    if (statementBlocks.size() > 0) {
                        DummyMethod method = this.makeFunction(statementBlocks, classBlock, methodBlock);
                        List<GeneratedFunction> thisFunctions = method.makeFunctions(true, existingFunctions);
                        if (thisFunctions.size() > 0) {
                            linesCovered.addAll(getLinesCovered(method));
                            functions.addAll(thisFunctions);
                        }
                    }
                } else {
                    for (List<StatementBlock> statementBlocks: methodBlock.getStatementGroups()) {
//                        if (statementBlocks.size() != 8)
//                            continue;
                        DummyMethod method = this.makeFunction(statementBlocks, classBlock, methodBlock);
//                        System.out.println("\n**** Combination **** ");
//                        for (StatementBlock statementBlock: statementBlocks) {
//                            System.out.println(statementBlock.getStatementAST());
//                        }
                        List<GeneratedFunction> thisFunctions = method.makeFunctions(true, existingFunctions);
//                        System.out.println(thisFunctions.size());
//                        System.out.println("***********************\n\n");
                        if (thisFunctions.size() > 0) {
                            linesCovered.addAll(getLinesCovered(method));
                            functions.addAll(thisFunctions);
                        }
                    }
                }
            }
        }
        LOGGER.info(String.format("Done. # Functions = %d", functions.size()));
        return functions;
    }

}
