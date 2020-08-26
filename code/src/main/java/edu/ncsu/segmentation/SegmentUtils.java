package edu.ncsu.segmentation;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import edu.ncsu.arguments.ObjectTypeArguments;
import edu.ncsu.config.hyperparameters.ConstructorExpansion;
import edu.ncsu.executors.helpers.FileHandler;
import edu.ncsu.executors.models.Function;
import edu.ncsu.executors.models.FunctionVariable;
import edu.ncsu.executors.models.Primitive;
import edu.ncsu.executors.models.SystemClassConstructor;
import edu.ncsu.utils.JavaFormatter;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.blocks.Imports;
import org.apache.commons.lang3.StringUtils;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Logger;

public class SegmentUtils {

    private final static Logger LOGGER = Logger.getLogger(Logger.class.getName());

    public static void writeFunctionsToFile(List<Function> functions, String packageName, String className, String writeFilePath) {
        List<String> funcStrings = new ArrayList<>();
        for (Function function: functions)
            funcStrings.add(function.toString());
        writeFunctionStringsToFile(funcStrings, packageName, className, writeFilePath);
    }

    public static void writeFunctionStringsToFile(List<String> functions , String packageName, String className, String writeFilePath) {
        if (functions.size() == 0) {
            LOGGER.info(String.format("Not writing to '%s' as there are no functions to write", Utils.getRepoLocalPath(writeFilePath)));
            return;
        }
        LOGGER.info(String.format("Writing '%d' functions for class '%s.%s' to '%s' ... ", functions.size(), packageName, className, Utils.getRepoLocalPath(writeFilePath)));
        StringBuilder javaContent = new StringBuilder();
        javaContent.append("package ").append(packageName).append(";\n\n").
                append(Imports.defaultImports()).
                append("public class ").append(className).append(" {\n");
        for (String function: functions) {
            javaContent.append(function).append("\n");
        }
        javaContent.append("}");
        File writeFile = new File(writeFilePath);
        try (PrintWriter out = new PrintWriter(writeFile)) {
            out.println(javaContent.toString());
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        JavaFormatter.formatAndSave(writeFilePath);
    }

    /**
     * Expand the arguments(List<FunctionVariable>' to a combination of all the possible constructors(List<List<FunctionVariable>>).
     * @param function - Function to be expanded.
     * @return - List of List of Function parameters where each inner list represents a combination of constructor.
     */
    public static List<List<FunctionVariable>> expandFunctionVariables(Function function, ConstructorExpansion constructorExpansion) {
        List<FunctionVariable> arguments = new ArrayList<>(function.getArguments());
        List<List<FunctionVariable>> allExpandedArgs = new ArrayList<>();
        for (FunctionVariable arg: arguments) {
            List<List<FunctionVariable>> allCopiedArgs = new ArrayList<>();
            List<FunctionVariable> thisExpandedArgs = expandFunctionVariable(arg, constructorExpansion);
            if (thisExpandedArgs == null)
                return null;
            for (FunctionVariable thisExpandedArg : thisExpandedArgs) {
                FunctionVariable copiedArg = FunctionVariable.clone(thisExpandedArg);
                if (allExpandedArgs.size() == 0) {
                    List<FunctionVariable> copiedArgs = new ArrayList<>();
                    copiedArgs.add(copiedArg);
                    allCopiedArgs.add(copiedArgs);
                } else {
                    for (List<FunctionVariable> expandedArgs : allExpandedArgs) {
                        List<FunctionVariable> copiedArgsCloned = new ArrayList<>(expandedArgs);
                        copiedArgsCloned.add(copiedArg);
                        allCopiedArgs.add(copiedArgsCloned);
                    }
                }
            }
            allExpandedArgs = allCopiedArgs;
        }
        // allExpandedObjectArgs contains combinations of all constructors for the methods.
        for (List<FunctionVariable> args: allExpandedArgs)
            args.sort(new FunctionVariable.FunctionArgComparator());
        return allExpandedArgs;
    }

    /***
     * Expand the function variable using its constructors
     * @param variable - Instance of FunctionVariable which needs to be expanded
     * @return - List of expanded function variables.
     */
    public static List<FunctionVariable> expandFunctionVariable(FunctionVariable variable, ConstructorExpansion constructorExpansion) {
        List<FunctionVariable> expanded = new ArrayList<>();
        if (isSystemClass(variable)) {
            JsonArray constructorArray = getConstructors(variable.getFullTypeKey(), constructorExpansion);
            if (constructorArray == null)
                return null;
            for (int constructorIndex = 0; constructorIndex < constructorArray.size(); constructorIndex++) {
                JsonObject constructor = constructorArray.get(constructorIndex).getAsJsonObject();
                if (constructor.has("parameters") && constructor.get("parameters").getAsJsonArray().size() > 0) {
                    List<List<FunctionVariable>> allExpandedConstructorParams = expandConstructorWithParams(constructor, constructorExpansion);
                    if (allExpandedConstructorParams == null)
                        return null;
                    for (List<FunctionVariable> expandedArgs: allExpandedConstructorParams) {
                        SystemClassConstructor systemClassConstructor = new SystemClassConstructor(constructor, expandedArgs);
                        FunctionVariable cloned = FunctionVariable.clone(variable);
                        cloned.setSystemClassConstructor(systemClassConstructor);
                        expanded.add(cloned);
                    }
                } else {
                    SystemClassConstructor systemClassConstructor = new SystemClassConstructor(constructor, new ArrayList<>());
                    FunctionVariable cloned = FunctionVariable.clone(variable);
                    cloned.setSystemClassConstructor(systemClassConstructor);
                    expanded.add(cloned);
                }
            }
        } else {
            expanded.add(FunctionVariable.clone(variable));
        }
        return expanded;
    }

    /***
     * Expand a constructor to permutations of its parameters using the constructor's JSON representation
     * @param constructor - Json representation of constructor
     * @return - List of List of function variables where the inner list represents an expansion of the function's arguments
     */
    private static List<List<FunctionVariable>> expandConstructorWithParams(JsonObject constructor, ConstructorExpansion constructorExpansion) {
        List<List<FunctionVariable>> allExpandedConstructorParams = new ArrayList<>();
        for (JsonElement param: constructor.getAsJsonArray("parameters")) {
            List<List<FunctionVariable>> allCopiedArgs = new ArrayList<>();
            JsonObject parameter = param.getAsJsonObject();
            List<FunctionVariable> expandedConstructorParams = expandFunctionVariable(parameter, constructorExpansion);
            if (expandedConstructorParams == null)
                return null;
            for (FunctionVariable thisExpandedConstructorParam: expandedConstructorParams) {
                FunctionVariable copiedArg = FunctionVariable.clone(thisExpandedConstructorParam);
                if (allExpandedConstructorParams.size() == 0) {
                    List<FunctionVariable> copiedArgs = new ArrayList<>();
                    copiedArgs.add(copiedArg);
                    allCopiedArgs.add(copiedArgs);
                } else {
                    for (List<FunctionVariable> expandedArgs : allExpandedConstructorParams) {
                        List<FunctionVariable> copiedArgsCloned = new ArrayList<>(expandedArgs);
                        copiedArgsCloned.add(copiedArg);
                        allCopiedArgs.add(copiedArgsCloned);
                    }
                }
            }
            allExpandedConstructorParams = allCopiedArgs;
        }
        return allExpandedConstructorParams;
    }

    /***
     * Helper function to validate if a FunctionVariable has a valid system class
     * @param var - Instance of FunctionVariable
     * @return - true if valid else false
     */
    private static boolean isSystemClass(FunctionVariable var) {
        String type = var.getFullTypeKey();
        if (!Primitive.isValidType(type) && !FileHandler.isInputOutputClass(type))
            return ObjectTypeArguments.isValidSystemClass(var.getFullTypeKey());
        return false;
    }

    /***
     * {
     * 	    "type" : "Dummy.area.Point",
     * 	    "name" : "a",
     * 	    "arrayDimensions" : 0
     * }
     * Expand function variable based on its Json representation
     * @param varJson - Json representation of a FunctionVariable.
     * @return - List of expanded function variables
     */
    public static List<FunctionVariable> expandFunctionVariable(JsonObject varJson, ConstructorExpansion constructorExpansion) {
        String type = varJson.get("type").getAsString();
        List<FunctionVariable> expanded = new ArrayList<>();
        if (!Primitive.isValidType(type) && !FileHandler.isInputOutputClass(type)) {
            JsonArray constructorArray = getConstructors(type, constructorExpansion);
            if (constructorArray == null)
                return null;
            for (int constructorIndex = 0; constructorIndex < constructorArray.size(); constructorIndex++) {
                JsonObject constructor = constructorArray.get(constructorIndex).getAsJsonObject();
                if (constructor.has("parameters") && constructor.get("parameters").getAsJsonArray().size() > 0) {
                    List<List<FunctionVariable>> allExpandedConstructorParams = expandConstructorWithParams(constructor, constructorExpansion);
                    if (allExpandedConstructorParams == null)
                        return null;
                    for (List<FunctionVariable> expandedArgs: allExpandedConstructorParams) {
                        SystemClassConstructor systemClassConstructor = new SystemClassConstructor(constructor, expandedArgs);
                        FunctionVariable cloned = new FunctionVariable(varJson, systemClassConstructor);
                        expanded.add(cloned);
                    }
                } else {
                    SystemClassConstructor systemClassConstructor = new SystemClassConstructor(constructor, new ArrayList<>());
                    FunctionVariable cloned = new FunctionVariable(varJson, null);
                    cloned.setSystemClassConstructor(systemClassConstructor);
                    expanded.add(cloned);
                }
            }
        } else {
            FunctionVariable cloned = new FunctionVariable(varJson, null);
            expanded.add(cloned);
        }
        return expanded;
    }

    /***
     * Return constructors for a class.
     * @param classKey - Key used to represent class. Look up {@link FunctionVariable`.`getFullNameOfType()} and ReflectionHelper.get
     * @param constructorExpansion - {@link ConstructorExpansion}
     * @return - List of constructors. The result varies based on the {@link ConstructorExpansion} parameter set in ProjectConfig
     */
    private static JsonArray getConstructors(String classKey, ConstructorExpansion constructorExpansion) {
        if (constructorExpansion == ConstructorExpansion.OPTIMAL) {
            JsonObject optimalConstructorJson = ObjectTypeArguments.getOptimalConstructorAsJson(classKey);
            if (optimalConstructorJson == null)
                return null;
            JsonArray constructors = new JsonArray();
            constructors.add(optimalConstructorJson);
            return constructors;
        } else if (constructorExpansion == ConstructorExpansion.ALL) {
            return ObjectTypeArguments.getConstructorsAsJson(classKey);
        } else {
            throw new RuntimeException(String.format("Invalid expansion mode for constructor => %s", constructorExpansion));
        }
    }

    /***
     * Create permutations of a list of function variables
     * @param sortedArgs - List of parameters of the function
     * @return - List of hash-maps where each hash-map contains a datatype and list of all variable names with the datatype.
     */
    public static List<Map<String, List<String>>> makePermutations(List<FunctionVariable> sortedArgs) {
        List<Map<String, List<String>>> permutations = new ArrayList<>();
        List<Map<String, String>> argKeyMaps = makeArgKeyMap(sortedArgs);
        if (argKeyMaps == null) {
            return permutations;
        }
        Map<String, List<String>> typeGroups = new HashMap<>();
        for (Map<String, String> argKeyMap : argKeyMaps) {
            String type = argKeyMap.get("key");
            String name = argKeyMap.get("name");
            if (typeGroups.containsKey(type)) {
                typeGroups.get(type).add(name);
            } else {
                List<String> names = new ArrayList<>();
                names.add(name);
                typeGroups.put(type, names);
            }
        }
        Map<String, List<List<String>>> typeGroupPermutations = new HashMap<>();
        for (String key: typeGroups.keySet()) {
            typeGroupPermutations.put(key, permutate(typeGroups.get(key)));
        }
        for (String type: typeGroupPermutations.keySet()) {
            List<List<String>> typePermutations = typeGroupPermutations.get(type);
            List<Map<String, List<String>>> thisPermutations = new ArrayList<>();
            for (List<String> typePermutation: typePermutations) {
                if (permutations.size() == 0) {
                    Map<String, List<String>> thisPermutation = new HashMap<>();
                    thisPermutation.put(type, typePermutation);
                    thisPermutations.add(thisPermutation);
                } else {
                    for (Map<String, List<String>> permutation: permutations) {
                        Map<String, List<String>> thisPermutation = new HashMap<>(permutation);
                        thisPermutation.put(type, typePermutation);
                        thisPermutations.add(thisPermutation);
                    }
                }
            }
            permutations = thisPermutations;
        }
        return permutations;
    }

    /***
     * Construct a list of type name map for a list of FunctionVariables
     * @param args - List of FunctionVariables
     * @return - List of map of expanded parameter names and arg types.
     */
    private static List<Map<String, String>> makeArgKeyMap(List<FunctionVariable> args) {
        List<Map<String, String>> argKeyMaps = new ArrayList<>();
        for (FunctionVariable arg: args) {
            List<Map<String, String>> paramArgAndKeys =  getArgAndKey(arg);
            if (paramArgAndKeys != null && paramArgAndKeys.size() > 0) {
                argKeyMaps.addAll(paramArgAndKeys);
            }
        }
        if (argKeyMaps.size() == 0)
            return null;
        return argKeyMaps;
    }


    /**
     * Construct a list of type name map for a FunctionVariable
     * @param arg - Instance of FunctionVariable
     * @return - List of map of expanded parameter names and arg types.
     */
    private static List<Map<String, String>> getArgAndKey(FunctionVariable arg) {
        String key, name = arg.getName();
        List<Map<String, String>> argKeyMaps = new ArrayList<>();
        if (arg.getPrimitive() != null) {
            key = arg.getPrimitive().getFamily().getName();
            Map<String, String> argKeyMap = new HashMap<>();
            argKeyMap.put("name", name);
            argKeyMap.put("key", key);
            argKeyMaps.add(argKeyMap);
        } else if (arg.isBuiltInType()) {
            key = arg.getFullTypeKey();
            if (FileHandler.isInputClass(key)) {
                key = FileHandler.FILE_INPUT_TYPE;
            } else if  (FileHandler.isOutputClass(key)) {
                key = FileHandler.FILE_OUTPUT_TYPE;
            }
            Map<String, String> argKeyMap = new HashMap<>();
            argKeyMap.put("name", name);
            argKeyMap.put("key", key);
            argKeyMaps.add(argKeyMap);
        } else if (arg.getSystemClassConstructor() != null) {
            String classKey = arg.getSystemClassConstructor().getJsonObject().get("classKey").getAsString();
            if (ObjectTypeArguments.isFinalClassObject(classKey)) {
                key = ObjectTypeArguments.OBJECT;
                Map<String, String> argKeyMap = new HashMap<>();
                argKeyMap.put("name", name);
                argKeyMap.put("key", key);
                argKeyMaps.add(argKeyMap);
            } else {
                if (arg.getSystemClassConstructor().getArguments() != null && arg.getSystemClassConstructor().getArguments().size() > 0) {
                    for (FunctionVariable constructorArg : arg.getSystemClassConstructor().getArguments()) {
                        List<Map<String, String>> paramArgAndKeys =  getArgAndKey(constructorArg);
                        if (paramArgAndKeys != null && paramArgAndKeys.size() > 0) {
                            for (Map<String, String> argKeyMap : paramArgAndKeys) {
                                argKeyMap.put("name", String.format("%s.%s", name, argKeyMap.get("name")));
                            }
                            argKeyMaps.addAll(paramArgAndKeys);
                        }
                    }
                } else {
                    return null;
                }
            }
        } else {
            throw new RuntimeException("Not a primitive, neither system class constructor. Check getArgAndKey.");
        }
        if (arg.getArrayDimensions() > 0) {
            List<String> keys = new ArrayList<>();
            for (Map<String, String> argKeyMap : argKeyMaps) {
                keys.add(argKeyMap.get("key"));
            }
            if (keys.size() == 0)
                return null;
            Map<String, String> argKeyMap = new HashMap<>();
            argKeyMap.put("name", name);
            argKeyMap.put("key", String.format("(%s)@%d", StringUtils.join(keys, ","), arg.getArrayDimensions()));
            argKeyMaps = new ArrayList<>();
            argKeyMaps.add(argKeyMap);
        }
        return argKeyMaps;
    }

    /***
     * Helper function to make permutation of a list of strings
     * @param args - List of args as string
     * @return - List of list all permutation of the args.
     */
    private static List<List<String>> permutate(List<String> args) {
        List<List<String>> permutations = new ArrayList<>();
        int n = args.size();
        int[] indexes = new int[n];
        for (int i=0; i < n; i++)
            indexes[i] = 0;
        List<String> cloned = new ArrayList<>(args);
        permutations.add(new ArrayList<>(cloned));
        int i = 0;
        while (i < n) {
            if (indexes[i] < i) {
                swap(cloned, i % 2 == 0 ? 0 : indexes[i], i);
                permutations.add(new ArrayList<>(cloned));
                indexes[i]++;
                i = 0;
            } else {
                indexes[i] = 0;
                i++;
            }
        }
        return permutations;
    }

    /***
     * Helper function to swap two indexes of a list in place.
     * @param lst - List of strings
     * @param a - first index of swap
     * @param b - second index of swap
     */
    private static void swap(List<String> lst, int a, int b) {
        assert lst != null;
        String tmp = lst.get(a);
        lst.set(a, lst.get(b));
        lst.set(b, tmp);
    }

}
