package edu.ncsu.segmentation;

import com.google.common.base.Joiner;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.config.hyperparameters.ConstructorExpansion;
import edu.ncsu.config.hyperparameters.HyperParameters;
import edu.ncsu.executors.models.*;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.utils.MavenUtils;
import edu.ncsu.utils.Utils;
import org.apache.commons.lang3.StringUtils;

import java.lang.reflect.Method;
import java.util.*;
import java.util.logging.Logger;


public class Permutator {

    private static Logger LOGGER = Logger.getLogger(Permutator.class.getName());

    private static boolean hasTooManyArguments(List<FunctionVariable> arguments) {
        int argCount = 0;
        for (FunctionVariable argument : arguments)
            argCount += argument.getSystemClassConstructor() != null ? argument.getSystemClassConstructor().getTotalArguments() : 0;
        return argCount > HyperParameters.MAX_NUM_ARGS;
    }


    /***
     * Generate all permutations of a function.
     * @param function - Function object whose arguments are permutated
     * @param metadataStore - IMetadataStore object which is used to lookup metadata for the function
     * @param permutatedFile - Path to write the permutated functions.
     * @return - Map containing the metadata of permutated functions and the functions as strings.
     */
    private static Map<String, Object> permutateFunction(Function function, IMetadataStore metadataStore, String permutatedFile, ConstructorExpansion constructorExpansion) {
        if (function.shouldBeSkipped() || !function.getAst().getBody().isPresent())
            return null;
        Method method = function.getMethod();
        JsonObject metadata = metadataStore.getFunctionMetadata(function.getName());
        assert  metadata != null;
        metadata.remove("_id");
        String body = function.getAst().getBody().get().toString();
        String returnType = Function.getMethodReturnTypeAsString(method);
        List<List<FunctionVariable>> argsPermutation = SegmentUtils.expandFunctionVariables(function, constructorExpansion);
        if (argsPermutation == null)
            return null;
        List<JsonObject> functionsMetadata = new ArrayList<>();
        List<String> functionsAsString = new ArrayList<>();
        JsonObject returnMeta = function.getReturnMetadata();
        for (List<FunctionVariable> args: argsPermutation) {
            if (hasTooManyArguments(args)) {
                LOGGER.info("Too many arguments found ... ");
                continue;
            }
            List<String> argsAsStr = new ArrayList<>();
            for (FunctionVariable arg: args)
                argsAsStr.add(arg.toFunctionParameter());
            String argStr = StringUtils.join(argsAsStr,  ", ");
            JsonArray argsMetadata = new JsonArray();
            for (FunctionVariable arg: args) {
                argsMetadata.add(arg.getMetadataAsJson());
            }
            Set<String> existingFunctions = new HashSet<>();
            for (Map<String, List<String>> permutation: SegmentUtils.makePermutations(args)) {
                String serializedPermutation = serializeMap(permutation);
                if (existingFunctions.contains(serializedPermutation))
                    continue;
                existingFunctions.add(serializedPermutation);
                String functionName = "func_" + Utils.randomString();
                String functionAsString = String.format("public static %s %s(%s)%s", returnType, functionName, argStr, body);
                JsonObject cloned = metadata.deepCopy();
                cloned.addProperty("name", functionName);
                cloned.addProperty("originalFunctionName", metadata.get("name").getAsString());
                cloned.addProperty("body", functionAsString);
                cloned.addProperty("inputKey", Function.makeArgumentsKey(permutation));
                cloned.addProperty("filePath", Utils.getRepoLocalPath(permutatedFile));
                cloned.add("argsMetadata", argsMetadata);
                cloned.add("argsPermutation", Function.encodeArgsPermutation(permutation));
                cloned.add("returnMetadata", returnMeta);
                functionsMetadata.add(cloned);
                functionsAsString.add(functionAsString);
            }
        }
        Map<String, Object> retData = new HashMap<>();
        retData.put("metadata", functionsMetadata);
        retData.put("functionsAsString", functionsAsString);
        return retData;
    }

    /***
     * Permutate all functions in the file
     * @param dataset - Dataset under study
     * @param generatedFile - Path to file containing generated functions
     * @param force - If true, redoes permutation.
     * - Writes all permutated functions in a permutated file.
     */
    @SuppressWarnings("unchecked")
    public static void permutateFile(String dataset, String generatedFile, boolean force) {
        IMetadataStore metadataStore = BaseStorage.loadMetadataStore(dataset);
        String fileName = Utils.getFileName(generatedFile);
        if (!fileName.startsWith(Settings.GENERATED_CLASS_PREFIX)) {
            LOGGER.info(String.format("%s is not a generated file. Not permutating!", generatedFile));
            return;
        }
        String parentFolder = Utils.getFolderPath(generatedFile);
        String suffix = fileName.substring(Settings.GENERATED_CLASS_PREFIX.length());
        String className = Settings.PERMUTATED_CLASS_PREFIX + suffix.split(".java")[0];
        String permutatedFile = Utils.pathJoin(parentFolder, className + ".java");
        if (Utils.fileExists(permutatedFile) && !force) {
            LOGGER.info(String.format("Processed file: %s. Moving on ...", generatedFile));
            return;
        }
        metadataStore.deleteClassFunctionsMetadata(Utils.getRepoLocalPath(permutatedFile));
        ClassMethods classMethods = new ClassMethods(dataset, generatedFile);
        LOGGER.info(String.format("Permutating '%d' functions ... ", classMethods.getMethods().size()));
        List<String> functionsAsString = new ArrayList<>();
        List<JsonObject> functionsMetadata = new ArrayList<>();
        classMethods.getMethods().forEach(
                (methodName, method) -> {
//                    if (!methodName.equals("func_c2a9adb34d944a2a89e4f9242676c470"))
//                        return;
                    Function function = classMethods.getFunction(method.getName());
                    if (function == null)
                        return;
                    Map<String, Object> permFunctionData = permutateFunction(function, metadataStore, permutatedFile, HyperParameters.CONSTRUCTOR_EXPANSION);
                    if (permFunctionData == null) {
                        LOGGER.severe(String.format("Skipping function: %s since it returns null on permutation of args. Debug permutateFunction method!", function.getName()));
                        return;
                    }
                    functionsMetadata.addAll((List<JsonObject>) permFunctionData.get("metadata"));
                    functionsAsString.addAll((List<String>) permFunctionData.get("functionsAsString"));
                }
        );
        SegmentUtils.writeFunctionStringsToFile(functionsAsString, classMethods.getPackageName(), className, permutatedFile);
        metadataStore.saveClassFunctionsMetadata(functionsMetadata);
    }

    private static String serializeMap(Map<String, List<String>> javaObj) {
        if (javaObj == null || javaObj.isEmpty())
            return "{}";
        StringBuilder sb = new StringBuilder();
        sb.append("{");
        List<String> sortedKeys = new ArrayList<>(javaObj.keySet());
        Collections.sort(sortedKeys);
        int i = 0;
        for (String key: sortedKeys) {
            i += 1;
            sb.append(key).append(":[").append(Joiner.on(",").join(javaObj.get(key))).append("]");
            if (i != sortedKeys.size())
                sb.append(",");
        }
        sb.append("}");
        return sb.toString();
    }

    public static void main(String[] args) {
        String fileName = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/Y14R5P1/Aksenov/generated_class_f4d3689ab1814176bc32bee46aaa117b.java";
//        String fileName = "/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/guava/src/com/google/common/base/generated_class_12af19636da4479b8625af5a252ae52e.java";
        permutateFile(ProjectConfig.DATASET, fileName, true);
        MavenUtils.buildProject();
//        System.out.println("Hello " + 5);
    }
}
