package edu.ncsu.engines;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.config.hyperparameters.ConstructorExpansion;
import edu.ncsu.config.hyperparameters.HyperParameters;
import edu.ncsu.executors.ExecutionResult;
import edu.ncsu.executors.ExecutionUtils;
import edu.ncsu.executors.models.Function;
import edu.ncsu.executors.models.FunctionVariable;
import edu.ncsu.segmentation.SegmentUtils;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.helpers.VisitorHelper;
import org.joor.CompileOptions;
import org.joor.Reflect;

import java.io.*;
import java.lang.reflect.Method;
import java.util.*;
import java.util.logging.Logger;

public class Execution {

    private static Logger LOGGER = Logger.getLogger(Execution.class.getName());

    public static String BASE_PACKAGE = "edu.ncsu.samples";

    public static final String JAVA_FOLDER = Utils.pathJoin(Settings.CODE_HOME, "src", "main", "java");

    private final static CompileOptions COMPILER_OPTIONS = new CompileOptions().options("-nowarn", "-parameters", "-classpath", System.getProperty("java.class.path"));

    private final static IMetadataStore METADATA_STORE = BaseStorage.loadMetadataStore(ProjectConfig.DATASET);

    public static String createRandomClassName() {
        return String.format("Class_%s", Utils.randomString());
    }

    public static Class<?> loadClass(String content, String className) {
        Reflect reflect = Reflect.compile(String.format("%s.%s", BASE_PACKAGE, className), content, COMPILER_OPTIONS).create();
        return reflect.type();
    }

    public static List<String> loadFunctions(String javaFunctionPath) {
        JsonParser parser = new JsonParser();
        File functionFile = new File(javaFunctionPath);
        try {
            if (!functionFile.exists()) {
                return null;
            }
            JsonArray array = parser.parse(new FileReader(functionFile)).getAsJsonArray();
            List<String> functionBodies = new ArrayList<>();
            for (JsonElement functionBody: array) {
                functionBodies.add(functionBody.getAsString());
            }
            return functionBodies;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static MethodDeclaration getFunctionAST(String classContent) {
        CompilationUnit compilationUnit = VisitorHelper.parseContent(classContent);
        return compilationUnit.getTypes().get(0).getMethods().get(0);
    }

    public static Map<String, String> createClassFile(String functionBody) {
        StringBuilder cb = new StringBuilder();
        String className = createRandomClassName();
        cb.append(String.format("package %s;\n", BASE_PACKAGE));
        cb.append("import java.util.*;\n\n");
        cb.append(String.format("public class %s {\n %s \n}", className, functionBody));
        String filePath = Utils.pathJoin(JAVA_FOLDER,
                BASE_PACKAGE.replace(".", File.separator),
                String.format("%s.java", className));
        String classBody = cb.toString();
        Map<String, String> meta = new HashMap<>();
        meta.put("className", className);
        meta.put("classContent", classBody);
        meta.put("filePath", filePath);
        return meta;
    }

    public static Function createFunction(String functionBody) {
        Map<String, String> meta = createClassFile(functionBody);
        Class<?> clazz = loadClass(meta.get("classContent"), meta.get("className"));
        MethodDeclaration ast = getFunctionAST(meta.get("classContent"));
        String methodName = ast.getNameAsString();
        Method method = null;
        for (Method m: clazz.getMethods()) {
            if (m.getName().equals(methodName)) {
                method = m;
                break;
            }
        }
        if (method == null) {
            LOGGER.severe(String.format("@COSAL: Failed to find method '%s' in compiled class. Most likely the method was not declared as 'static'!", methodName));
            return null;
        }
        Function function = new Function(ProjectConfig.DATASET, method, ast, meta.get("filePath"));
        if (function.getArguments().size() == 0) {
            LOGGER.severe(String.format("@COSAL: Method '%s' has no arguments!", methodName));
            return null;
        }
        List<List<FunctionVariable>> argsPermutation = SegmentUtils.expandFunctionVariables(function, ConstructorExpansion.OPTIMAL);
        if (argsPermutation == null)
            throw new RuntimeException("@COSAL: Failed to create permutation. Check the function");
        function.setArguments(argsPermutation.get(0));
        JsonArray argsMetadata = new JsonArray();
        for (FunctionVariable arg: function.getArguments()) {
            argsMetadata.add(arg.getMetadataAsJson());
        }
        JsonObject metadata = new JsonObject();
        metadata.addProperty("name", function.getName());
        metadata.addProperty("project", ProjectConfig.PROJECT_NAME);
        metadata.addProperty("originalFunctionName", function.getName());
        metadata.addProperty("body", functionBody);
        metadata.addProperty("filePath", meta.get("filePath"));
        Map<String, List<String>> argPermutation = SegmentUtils.makePermutations(function.getArguments()).get(0);
        metadata.addProperty("inputKey", Function.makeArgumentsKey(argPermutation));
        metadata.add("argsMetadata", argsMetadata);
        metadata.add("argsPermutation", Function.encodeArgsPermutation(argPermutation));
        metadata.add("returnMetadata", function.getReturnMetadata());
        function.setMetadata(metadata);
        METADATA_STORE.saveClassFunctionMetadata(metadata);
        return function;
    }

    public static void executeFunctionBody(String functionBody) {
        // 1. Generate Function Object
        Function function = createFunction(functionBody);
        if (function == null)
            return;
        // 2. Load Arguments
        List<Object[]> arguments = ExecutionUtils.loadArguments(function, HyperParameters.FUZZ_ARGUMENT_SIZE);
        if (arguments == null || arguments.size() == 0)
            throw new RuntimeException(String.format("@COSAL: Unable to generate arguments for the function: %s", function.getName()));
        // 3. Execute functions
        List<ExecutionResult> executionResults;
        try {
            executionResults = ExecutionUtils.executeFunction(function, arguments);
            if (executionResults == null || executionResults.size() == 0)
                throw new RuntimeException(String.format("Exception while executing function: %s", function.getName()));
        } catch (Exception e) {
            throw new RuntimeException(String.format("Exception while executing function: %s", function.getName()));
        }
        JsonObject executedFunction = ExecutionUtils.executeFunctionAsJSON(function, arguments);
        ExecutionUtils.storeFunction(executedFunction);
        if (executedFunction.has("outputs")) {
            LOGGER.info(String.format("Saved function results of '%s' in table 'functions_executed'", function.getName()));
        } else if (executedFunction.has("errorTrace")) {
            LOGGER.info(String.format("Saved function error of '%s' in table 'functions_failed'", function.getName()));
        }
        ExecutionUtils.shutdownExecutor();
    }

    public static void executeBodies(String functionsPath) {
        List<String> functionBodies = loadFunctions(functionsPath);
        int functionIndex = 0;
        for (String functionBody: functionBodies) {
            functionIndex += 1;
            LOGGER.info(String.format("PROCESSING FUNCTION %d / %d .... ", functionIndex, functionBodies.size()));
            executeFunctionBody(functionBody);
        }
    }

    public static void test() {
        String functionBody = "public static void CountbyChar (String s) {\n    int [] arr = new int [256];\n    for (char c : s.toCharArray ()) {\n        if (c < 256) {\n            arr [c] ++;\n        }\n    }\n    for (int i = 0;\n    i != 256; i ++) {\n        if (arr [i] != 0) {\n            System.out.print ((char) i);\n            System.out.print (\" : \");\n            System.out.println (arr [i]);\n        }\n    }\n}";
        executeFunctionBody(functionBody);
    }


    public static void main(String[] args) {
        if (args.length < 1) {
            LOGGER.severe("<FilePath> should be the first argument!");
            System.exit(0);
        }
//        String functionsPath = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_expts/sample_functions.json";
        String functionsPath = args[0];
        executeBodies(functionsPath);
    }

}


