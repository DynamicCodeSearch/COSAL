package edu.ncsu.arguments;

import edu.ncsu.config.ProjectConfig;
import edu.ncsu.executors.helpers.FileHandler;
import edu.ncsu.executors.models.*;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IArgumentStore;
import edu.ncsu.config.hyperparameters.HyperParameters;
import edu.ncsu.utils.Utils;
import org.apache.commons.lang3.NotImplementedException;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.concurrent.ThreadLocalRandom;
import java.util.logging.Logger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;

public class ArgumentGenerator {

    private static final Logger LOGGER = Logger.getLogger(ArgumentGenerator.class.getName());


    private final static IArgumentStore ARGUMENT_STORE = BaseStorage.loadArgumentStore(ProjectConfig.DATASET, ProjectConfig.IS_FALSE_POSITIVE_TESTING);

    public static IArgumentStore getStore() {
        return ARGUMENT_STORE;
    }

    // *********************************************************************************** //
    // PRIMITIVES

    /**
     * @return - A random short value
     */
    private static Short randShort() {
        double probability = Math.random();
        if (probability < 0.1) {
            return randShort(-10, 10);
        } else if (probability < 0.7) {
            return randShort(-100, 100);
        } else if (probability < 0.9) {
            return randShort(-1000, 1000);
        } else {
            return randShort(Short.MIN_VALUE/2, Short.MAX_VALUE/2);
        }
    }

    /**
     * @param low - Low value of range
     * @param high - High value of range
     * @return - Random short value in a range
     */
    private static Short randShort(Integer low, Integer high) {
        return randInteger(low, high).shortValue();
    }


    /**
     * @return - A random integer value
     */
    private static Integer randInteger() {
        double probability = Math.random();
        if (probability < 0.1) {
            return randInteger(-10, 10);
        } else if (probability < 0.7) {
            return randInteger(-100, 100);
        } else if (probability < 0.9) {
            return randInteger(-1000, 1000);
        } else {
            return randInteger((Integer.MIN_VALUE + 2)/2, Integer.MAX_VALUE/2);
        }
    }

    /**
     * @param low - Low value of range
     * @param high - High value of range
     * @return - Random integer value in range.
     */
    private static Integer randInteger(Integer low, Integer high) {
        return ThreadLocalRandom.current().nextInt(low, high + 1);
    }

    /**
     * @return - random long value
     */
    private static Long randLong() {
        double probability = Math.random();
        if (probability < 0.1) {
            return randLong(-10L, 10L);
        } else if (probability < 0.7) {
            return randLong(-100L, 100L);
        } else if (probability < 0.9) {
            return randLong(-1000L, 1000L);
        } else {
            return randLong((Long.MIN_VALUE + 2)/2, Long.MAX_VALUE/2);
        }
    }

    /**
     * @param low - Low value of range
     * @param high - High value of range
     * @return - Return a random long value
     */
    private static Long randLong(Long low, Long high) {
        return ThreadLocalRandom.current().nextLong(low, high + 1);
    }

    /**
     * @return - A random float value
     */
    private static Float randFloat() {
        double probability = Math.random();
        if (probability < 0.1) {
            return randFloat(-10.0f, 10.0f);
        } else if (probability < 0.7) {
            return randFloat(-100.0f, 100.0f);
        } else if (probability < 0.9) {
            return randFloat(-1000.0f, 1000.0f);
        } else {
            return randFloat((Float.MIN_VALUE + 2)/2, Float.MAX_VALUE/2);
        }
    }

    /**
     * Return
     * @param low - low value of range
     * @param high - high value of range
     * @return - Random float in range
     */
    private static Float randFloat(Float low, Float high) {
        return (float) ThreadLocalRandom.current().nextDouble(low, high + 1);
    }

    /**
     * @return - A random double value
     */
    private static Double randDouble() {
        double probability = Math.random();
        if (probability < 0.1) {
            return randDouble(-10.0, 10.0);
        } else if (probability < 0.7) {
            return randDouble(-100.0, 100.0);
        } else if (probability < 0.9) {
            return randDouble(-1000.0, 1000.0);
        } else {
            return randDouble((Double.MIN_VALUE + 2)/2, Double.MAX_VALUE/2);
        }
    }

    /**
     * Return
     * @param low - low value of range
     * @param high - high value of range
     * @return - Random double in range
     */
    private static Double randDouble(Double low, Double high) {
        return ThreadLocalRandom.current().nextDouble(low, high + 1);
    }

    /**
     * @return - A random boolean
     */
    private static Boolean randBoolean() {
        return ThreadLocalRandom.current().nextBoolean();
    }

    private static Object generateRandomArgument(Primitive argumentType) {
        switch (argumentType) {
            case SHORT:
                return randShort();
            case INTEGER:
                return randInteger();
            case LONG:
                return randLong();
            case FLOAT:
                return randFloat();
            case DOUBLE:
                return randDouble();
            case BOOLEAN:
                return randBoolean();
            case CHARACTER:
                return ArgumentMeta.randCharacter();
            case STRING:
                return ArgumentMeta.randString();
            default:
                throw new RuntimeException(String.format(
                        "Currently we do not support the class %s", argumentType.getName()));
        }
    }

    private static Object generateRandomArgumentForFamily(Primitive argumentType) {
        // TODO - modify this to query from DB
        Primitive.Family family = argumentType.getFamily();
        switch (family) {
            case INT_FAMILY:
                return randShort();
            case FLOAT_FAMILY:
                return randFloat();
            case BOOLEAN_FAMILY:
                return randBoolean();
            case CHAR_FAMILY:
                return ArgumentMeta.randCharacter();
            case STRING_FAMILY:
                return ArgumentMeta.randString();
            default:
                throw new RuntimeException(String.format(
                        "Currently we do not support the class %s", argumentType.getName()));
        }
    }

    // *********************************************************************************** //
    // Objects and Functions


    /**
     * Generate args for the function and argsKey and store in the store
     * @param function - Function object used to generate arguments
     * @param numArgs - Number of arguments to be generated
     */
    public static void generateAndStoreArgumentsForFunctionIfNotExists(Function function, int numArgs) {
        String argsKey = function.getArgumentsKey();
        if (ARGUMENT_STORE.fuzzedKeyExists(argsKey))
            return;
        LOGGER.info(String.format("Storing Key: %s", argsKey));
        try {
            List<Map<String, List<Object>>> arguments = generateArgumentsForFunctionBasedOnPermutation(function, numArgs);
            if (arguments != null) {
                ARGUMENT_STORE.saveFuzzedArguments(argsKey, arguments);
            }
        } catch (RuntimeException e) {
            LOGGER.severe(e.getMessage());
            e.printStackTrace();
        }
    }

    private static Object generateGreyboxArgumentForFamily(Primitive argumentType) {
        List<Object> args;
        Set<Object> existingPrimitives = ARGUMENT_STORE.loadPrimitiveArgumentsForName(argumentType);
        if (existingPrimitives == null) {
            args = new ArrayList<>();
        } else {
            args = new ArrayList<>(existingPrimitives);
        }
        while (args.size() < HyperParameters.SAMPLE_ARGUMENT_SIZE) {
            args.add(generateRandomArgumentForFamily(argumentType));
        }
        int randomIndex = new Random().nextInt(args.size());
        return args.get(randomIndex);
    }

    public static String generateString(ArgumentMeta meta) {
        String generatedString;
        if (meta.hasSeenString()) {
            generatedString = meta.getStringMutation();
        } else {
            generatedString = generateGreyboxArgumentForFamily(Primitive.STRING).toString();
        }
        meta.updateSeenStrings(generatedString);
        return generatedString;
    }

    private static Map<Integer, Integer> makeArrayDimensionSizes(int arrayDimensions) {
        Map<Integer, Integer> arrayDimensionSizes = new HashMap<>();
        if (arrayDimensions <= 0)
            return arrayDimensionSizes;
        int maxArrayDimensions = Integer.max(10, HyperParameters.MAX_ARRAY_SIZE / (arrayDimensions * arrayDimensions));
        while (arrayDimensions > 0) {
            arrayDimensionSizes.put(arrayDimensions, randInteger(2, maxArrayDimensions));
            arrayDimensions -= 1;
        }
        return arrayDimensionSizes;
    }

    public static List<Map<String, List<Object>>> generateArgumentsForFunctionBasedOnPermutation(Function function, int numArgs) {
        if (!function.isValidArgs()) {
            LOGGER.info(String.format("%s does not contain valid arguments", function.getName()));
            return null;
        }
        Map<String, List<String>> argPermutation = Function.decodeArgsPermutation(function.getMetadata().getAsJsonObject("argsPermutation"));
        List<String> keys = new ArrayList<>(argPermutation.keySet());
        List<String> argKeys = new ArrayList<>();
        for (String key: keys) {
            for (int i=0; i < argPermutation.get(key).size(); i++) {
                argKeys.add(key);
            }
        }
        return generateArgumentsForArgKeys(argKeys, numArgs);
    }

    public static List<Map<String, List<Object>>> generateArgumentsForFunctionKey(String functionKey, int numArgs) {
        List<String> argKeys = getArgKeys(functionKey);
        if (argKeys.size() == 0) {
            LOGGER.info(String.format("Function key '%s' does not contain valid argument keys ...", functionKey));
            return null;
        }
        return generateArgumentsForArgKeys(argKeys, numArgs);
    }

    private static List<Map<String, List<Object>>> generateArgumentsForArgKeys(List<String> argKeys, int numArgs) {
        List<Map<String, List<Object>>> arguments = new ArrayList<>();
        for (int i=0; i < numArgs; i++) {
            ArgumentMeta argumentMeta = new ArgumentMeta();
            Map<String, List<Object>> generatedArguments= new HashMap<>();
            for (String key: argKeys) {
                Map<String, Object> keyAndArraySize = extractKeyAndArraySize(key);
                int arrayDimensions = (Integer) keyAndArraySize.get("arrayDimensions");
                Map<Integer, Integer> arrayDimensionSizes = makeArrayDimensionSizes(arrayDimensions);
                // TODO: Change this to handle multidimensional arrays
                Map<String, Object> generatedArgumentsForKey = generateArgumentForKey((String) keyAndArraySize.get("key"), arrayDimensions, argumentMeta, arrayDimensionSizes);
                if (generatedArgumentsForKey != null) {
                    boolean isArray = (Boolean) generatedArgumentsForKey.get("isArray");
                    List<Object> existingGeneratedArgs = new ArrayList<>();
                    if (generatedArguments.containsKey(key)) {
                        existingGeneratedArgs = generatedArguments.get(key);
                    }
                    if (isArray) {
                        existingGeneratedArgs.add(generatedArgumentsForKey.get("args"));
                    } else {
                        existingGeneratedArgs.addAll((List) generatedArgumentsForKey.get("args"));
                    }
                    generatedArguments.put(key, existingGeneratedArgs);
                }
            }
            if (generatedArguments.size() == 0)
                return null;
            arguments.add(generatedArguments);
        }
        Collections.shuffle(arguments);
        return arguments;
    }

    private static Map<String, Object> generateArgumentForKey(String key, int arraySize, ArgumentMeta argMeta, Map<Integer, Integer> arrayDimensionSizes) {
        Map<String, Object> argsMap = new HashMap<>();
        List<Object> args = new ArrayList<>();
        boolean isArray = false;
        if (arraySize == 0) {
            List<String> subKeys = extractKeys(key);
            if (subKeys.size() == 1) {
                String subKey = subKeys.get(0);
                Map<String, Object> keyAndArraySize = extractKeyAndArraySize(subKey);
                int subKeyArrayDimensions = (Integer) keyAndArraySize.get("arrayDimensions");
                subKey = keyAndArraySize.get("key").toString();
                if (subKeyArrayDimensions == 0) {
                    Primitive primitive = Primitive.Family.getPrimitiveForFamily(subKey);
                    if (primitive != null) {
                        args.add(generatePrimitive(primitive, argMeta));
                    } else if (subKey.equals(ObjectTypeArguments.OBJECT)) {
                        args.add(generatePrimitive(Primitive.getRandomPrimitive(), argMeta));
                    } else if (FileHandler.isInputType(subKey) || FileHandler.isInputClass(subKey)) {
                        args.add(getFileContent(argMeta));
                    } else if (FileHandler.isOutputType(subKey) || FileHandler.isOutputClass(subKey)) {
                        args.add("");
                    } else {
                        throw new RuntimeException(String.format("Unsupported argument type: '%s'", subKey));
                    }
                } else {
                    isArray = true;
                    Map<Integer, Integer> subKeyArrayDimensionSizes = makeArrayDimensionSizes(subKeyArrayDimensions);
                    for (int i = 0; i < subKeyArrayDimensionSizes.get(subKeyArrayDimensions); i++) {
                        Map<String, Object> arrArgsForKey;
                        if (subKey.equals(ObjectTypeArguments.OBJECT)) {
                            arrArgsForKey = generateArgumentForKey(Primitive.getRandomPrimitive().getFamily().getName(), subKeyArrayDimensions - 1, argMeta, subKeyArrayDimensionSizes);
                        } else {
                            arrArgsForKey = generateArgumentForKey(subKey, subKeyArrayDimensions - 1, argMeta, subKeyArrayDimensionSizes);
                        }
                        if (arrArgsForKey == null)
                            return null;
                        args.add(arrArgsForKey.get("args"));
                    }
                }
            } else {
                for (String subKey: subKeys) {
                    Map<String, Object> keyAndArraySize = extractKeyAndArraySize(subKey);
                    int subKeyArrayDimensions = (Integer) keyAndArraySize.get("arrayDimensions");
                    Map<Integer, Integer> subKeyArrayDimensionSizes = makeArrayDimensionSizes(subKeyArrayDimensions);
                    subKey = keyAndArraySize.get("key").toString();
                    Map<String, Object> subKeyArgs = generateArgumentForKey(subKey, subKeyArrayDimensions, argMeta, subKeyArrayDimensionSizes);
                    if (subKeyArgs != null) {
                        if ((Boolean) subKeyArgs.get("isArray")) {
                            args.add(subKeyArgs.get("args"));
                        } else {
                            args.addAll((List) subKeyArgs.get("args"));
                        }
                    }
                }
                if (args.size() == 0)
                    return null;

            }
        } else {
            isArray = true;
            for (int i=0; i < arrayDimensionSizes.get(arraySize); i++) {
                Map<String, Object> arrArgsForKey;
                if (key.equals(ObjectTypeArguments.OBJECT)) {
                    arrArgsForKey = generateArgumentForKey(Primitive.getRandomPrimitive().getFamily().getName(), arraySize - 1, argMeta, arrayDimensionSizes);
                } else {
                    arrArgsForKey = generateArgumentForKey(key, arraySize - 1, argMeta, arrayDimensionSizes);
                }
                if (arrArgsForKey == null)
                    return null;
                args.add(arrArgsForKey.get("args"));
            }
        }
        argsMap.put("args", args);
        argsMap.put("isArray", isArray);
        return argsMap;
    }

    private static Object generatePrimitive(Primitive primitive, ArgumentMeta argMeta) {
        if (primitive.isStringFamily()) {
            return generateString(argMeta);
        } else {
            return generateGreyboxArgumentForFamily(primitive);
        }
    }

    public static String getFileContent(ArgumentMeta argumentMeta) {
        String inputFolder = null;
        try {
            inputFolder = ProjectConfig.getSeedFileInputsFolder();
        } catch (NotImplementedException ignored) {}
        if (inputFolder == null) {
            return getRandomFileContent(argumentMeta);
        } else {
            return getGeneratedFileContent(inputFolder);
        }
    }

    private static String getGeneratedFileContent(String inputFolder) {
        List<String> seedFiles = Utils.listFilesWithExtension(inputFolder, ".in", true, false, null);
        Path randomFilePath = Paths.get(seedFiles.get(new Random().nextInt(seedFiles.size())));
        try {
            Stream<String> contentStream = Files.lines(randomFilePath);
            Object[] contents = contentStream.toArray();
            int snipLength = new Random().nextInt(contents.length);
            StringBuilder content = new StringBuilder();
            int contentIndex = 0;
            while (contentIndex < snipLength + 1) {
                content.append(contents[contentIndex]).append("\n");
                contentIndex += 1;
            }
            return content.toString();
        } catch (IOException e) {
            throw new RuntimeException(String.format("Error while reading '%s'", randomFilePath), e);
        }
    }


    public static String getRandomFileContent(ArgumentMeta argumentMeta) {
        StringBuilder contents = new StringBuilder();
        int contentIndex = 0, maxLength = 20;
        while (contentIndex < maxLength) {
            contents.append(generatePrimitive(Primitive.getRandomPrimitive(), argumentMeta)).append("\n");
            contentIndex += 1;
        }
        return contents.toString();
    }

    private static List<String> extractKeys(String grandKey) {
        List<String> keys = new ArrayList<>();
        int i = 0, n = grandKey.length();
        StringBuilder key = new StringBuilder();
        int bracketCount = 0;
        while (i < n) {
            char c = grandKey.charAt(i);
            if (c == ',' && bracketCount == 0) {
                keys.add(key.toString());
                key = new StringBuilder();
            } else if (c == '(') {
                key.append(c);
                bracketCount += 1;
            } else if (c == ')') {
                key.append(c);
                bracketCount -= 1;
                if (bracketCount == 0) {
                    i+=1;
                    while (i < n && grandKey.charAt(i) != ',') {
                        key.append(grandKey.charAt(i));
                        i+=1;
                    }
                    keys.add(key.toString());
                    key = new StringBuilder();
                }
            } else {
                key.append(c);
            }
            i++;
        }
        if (key.length() > 0) {
            keys.add(key.toString());
        }
        return keys;
    }

    private static Map<String, Object> extractKeyAndArraySize(String key) {
        Pattern arrayPattern = Pattern.compile("[(](.+)[)]@([0-9]+)");
        Matcher matcher = arrayPattern.matcher(key);
        Map<String, Object> keyAndArraySize = new HashMap<>();
        if (matcher.matches()) {
            keyAndArraySize.put("key", matcher.group(1));
            keyAndArraySize.put("arrayDimensions", Integer.parseInt(matcher.group(2)));
        } else {
            keyAndArraySize.put("key", key);
            keyAndArraySize.put("arrayDimensions", 0);
        }
        return keyAndArraySize;
    }

    private static List<String> getArgKeys(String functionKey) {
        List<String> argKeys = new ArrayList<>();
        String argKeysPatternString = "(([a-zA-Z_][a-zA-Z0-9_.]*|(\\(\\S+?\\)@\\d+))##(\\d+))";
        Pattern argKeyPattern = Pattern.compile(argKeysPatternString);
        Matcher matcher = argKeyPattern.matcher(functionKey);
        while (matcher.find()) {
            String key = matcher.group(2);
            int repeats = Integer.parseInt(matcher.group(4));
            for (int rep=0; rep<repeats; rep++)
                argKeys.add(key);
        }
        return argKeys;
    }

    public static void testFile() {
        ArgumentMeta argumentMeta = new ArgumentMeta();
//        String contents = getFileContent(argumentMeta);
//        System.out.println(contents);
        int arrayDimensions = 3;
        Map<Integer, Integer> arrayDimensionSizes = makeArrayDimensionSizes(arrayDimensions);
        List<List> args = (List<List>) generateArgumentForKey("int", arrayDimensions, argumentMeta, arrayDimensionSizes).get("args");
//        System.out.println(args);
        for (List arg: args) {
            System.out.println(arg.size());
        }
    }

    public static void main(String[] args) {
//        testFile();
//        System.out.println(extractKeys("float##2,string##1"));
//        System.out.println(extractKeys("(int)@1##2,int##1"));
        System.out.println(generateArgumentsForFunctionKey("(int)@2##2,(int)@1##2,int##1", 5));
        System.exit(0);
        System.out.println(generateArgumentsForFunctionKey("float##2,string##1", 5));
//        String s = "int,(int,int,(int)@1,int)@2,(string,int)@3";
//        extractKeys(s).forEach(ArgumentGenerator::extractKeyAndArraySize);
    }

}
