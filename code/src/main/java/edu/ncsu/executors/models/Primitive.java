package edu.ncsu.executors.models;

import com.google.gson.JsonElement;
import com.google.gson.JsonPrimitive;
import edu.ncsu.executors.helpers.ReflectionHelper;

import java.util.*;
import java.util.List;

public enum  Primitive {

    SHORT("short", 0, Family.INT_FAMILY, "short", "Short", "java.lang.Short"),
    INTEGER("integer", 1, Family.INT_FAMILY, "int", "integer", "Integer", "java.lang.Integer"),
    LONG("long", 2, Family.INT_FAMILY, "long", "Long", "java.lang.Long"),
    CHARACTER("character", 3, Family.CHAR_FAMILY, "char", "character", "Character", "java.lang.Character"),
    FLOAT("float", 4, Family.FLOAT_FAMILY, "float", "Float", "java.lang.Float"),
    DOUBLE("double", 5, Family.FLOAT_FAMILY, "double", "Double", "java.lang.Double"),
    BOOLEAN("boolean", 6, Family.BOOLEAN_FAMILY, "boolean", "Boolean", "java.lang.Boolean"),
    BYTE("byte", 7, Family.BYTE_FAMILY, "byte", "Byte", "java.lang.Byte"),
    STRING("string", 8, Family.STRING_FAMILY, "String", "java.lang.String", "string"),
    CHAR_SEQUENCE("char_sequence", 9, Family.STRING_FAMILY, "CharSequence", "java.lang.CharSequence");

    private final static Set<String> VOIDS = new HashSet<>(Arrays.asList("void", "Void", "java.lang.Void"));

    public enum Family {

        INT_FAMILY("int", 0),
        CHAR_FAMILY("char", 1),
        FLOAT_FAMILY("float", 2),
        BOOLEAN_FAMILY("boolean", 3),
        BYTE_FAMILY("byte", 4),
        STRING_FAMILY("string", 5);

        Family(String name, int index) {
            this.name = name;
            this.index = index;
        }

        private String name;

        private int index;

        public String getName() {
            return this.name;
        }

        public int getIndex() {
            return this.index;
        }

        public static Primitive getPrimitiveForFamily(String family) {
            switch (family) {
                case "int":
                    return INTEGER;
                case "char":
                    return CHARACTER;
                case "float":
                    return FLOAT;
                case "boolean":
                    return BOOLEAN;
                case "byte":
                    return BYTE;
                case "string":
                    return STRING;
                default:
//                    throw new RuntimeException(String.format("Unknown Family: %s", family));
                    return null;
            }
        }
    }

    /**
     * Mapping types to Primitive Enum.
     */
    private final static Map<String, Primitive> typeToPrimitiveMap = new HashMap<>();

    /**
     * Mapping names to Primitive Enum.
     */
    private final static Map<String, Primitive> nameToPrimitiveMap = new HashMap<>();

    /**
     * Name of enum
     */
    private String name;

    /***
     * Index of the enum
     */
    private int index;

    /***
     * General family of primitive datatype
     */
    private Family family;

    /**
     * List of types corresponding to the primitive.
     */
    private List<String> types;

    static {
        // Populating the maps
        for (Primitive dataType: Primitive.values()) {
            nameToPrimitiveMap.put(dataType.name, dataType);
            for (String className: dataType.getTypes())
                typeToPrimitiveMap.put(className, dataType);
        }
    }

    /**
     * @return - Name of the Primitive.
     */
    public String getName() {
        return name;
    }

    /**
     * @return - Index of the enum
     */
    public int getIndex() {
        return index;
    }

    /**
     * @return - Family of the Primitive
     */
    public Family getFamily() {
        return family;
    }

    /**
     * @return - Types for Primitive
     */
    public List<String> getTypes() {
        return types;
    }

    /**
     * Check if primitive is of the string family
     * @return - true if the primitive is from string family
     */
    public boolean isStringFamily() {
        return family.equals(Family.STRING_FAMILY);
    }

    /**
     * @param type - Type as string
     * @return - Return Primitive Enum for the type
     */
    public static Primitive getPrimitive(String type) {
        return typeToPrimitiveMap.get(type);
    }

    @SuppressWarnings("rawtypes")
    public static Primitive getPrimitive(Class type) {
        return getPrimitive(type.getSimpleName());
    }


    /**
     * @return - Random Primitive. Can be used in the case of generics
     */
    public static Primitive getRandomPrimitive() {
        Random random = new Random();
        Primitive randomPrimitive = values()[random.nextInt(values().length)];
        if (randomPrimitive.getFamily().equals(Family.BYTE_FAMILY))
            return getRandomPrimitive();
        return randomPrimitive;
    }

    /**
     * @param type - Type as string
     * @return - Return true if Primitive Enum exists for type
     */
    public static boolean isValidType(String type) {
        return typeToPrimitiveMap.containsKey(type);
    }

    /**
     * @param type - Type as class object
     * @return - Return true if Primitive Enum exists for type
     */
    @SuppressWarnings("rawtypes")
    public static boolean isValidType(Class type) {
        return isValidType(type.getSimpleName());
    }

    /**
     * @param name - Name of primitive
     * @return - Return Primitive Enum for the name
     */
    public static Primitive getPrimitiveByName(String name) {
        return nameToPrimitiveMap.get(name);
    }

    /**
     * Create an instance of Primitive Enum
     * @param name - Name of the Primitive Enum
     * @param types - variable args of all the types
     */
    Primitive(String name, int index, Family family, String... types) {
        this.name = name;
        this.index =index;
        this.family = family;
        this.types = new ArrayList<>(Arrays.asList(types));
    }

    /**
     *
     * @param primitive - Primitive Enum
     * @param argString - Value of argument
     * @return - Argument converted to
     */
    public static Object convertToArgument(Primitive primitive, String argString) {
        switch (primitive) {
            case SHORT:
                return (short) Double.parseDouble(argString);
            case INTEGER:
                return (int) Double.parseDouble(argString);
            case LONG:
                return (long) Double.parseDouble(argString);
            case CHARACTER:
                return argString.charAt(0);
            case FLOAT:
                return (float) Double.parseDouble(argString);
            case DOUBLE:
                return Double.parseDouble(argString);
            case BOOLEAN:
                return Boolean.parseBoolean(argString);
            case BYTE:
                return Byte.parseByte(argString);
            case STRING:
            case CHAR_SEQUENCE:
                return argString;
            default:
                throw new RuntimeException(String.format(
                        "Currently we do not support the class %s", primitive.getName()));
        }
    }

    public static Object convertToArgument(String argString) {
        try {
            return Long.parseLong(argString);
        } catch (Exception le) {
            try {
                return Double.parseDouble(argString);
            } catch (Exception de) {
                if (argString.equals("false") || argString.equals("true")) {
                    return Boolean.parseBoolean(argString);
                }
                return argString;
            }
        }
    }

    @SuppressWarnings("rawtypes")
    public static boolean isPrimitive(Class clazz) {
        return isPrimitive(ReflectionHelper.makeKey(clazz));
    }

    public static boolean isPrimitive(String classKey) {
        return isValidType(classKey);
    }

    public static JsonElement convertToArgumentJSON(Primitive primitive, String argString) {
        switch (primitive) {
            case SHORT:
                return new JsonPrimitive((short) Double.parseDouble(argString));
            case INTEGER:
                return new JsonPrimitive((int) Double.parseDouble(argString));
            case LONG:
                return new JsonPrimitive((long) Double.parseDouble(argString));
            case CHARACTER:
                return new JsonPrimitive(argString.charAt(0));
            case FLOAT:
                return new JsonPrimitive((float) Double.parseDouble(argString));
            case DOUBLE:
                return new JsonPrimitive(Double.parseDouble(argString));
            case BOOLEAN:
                return new JsonPrimitive(Boolean.parseBoolean(argString));
            case BYTE:
                return new JsonPrimitive(Byte.parseByte(argString));
            case STRING:
                return new JsonPrimitive(argString.replaceAll("^\"|\"$", ""));
            default:
                throw new RuntimeException(String.format(
                        "Currently we do not support the class %s", primitive.getName()));
        }
    }

    /**
     * Get class of primitive type
     * @param primitive - Enum of primitive
     * @return - Class of primitive type
     */
    @SuppressWarnings("rawtypes")
    public static Class getPrimitiveClass(Primitive primitive) {
        switch (primitive) {
            case SHORT:
                return short.class;
            case INTEGER:
                return int.class;
            case LONG:
                return long.class;
            case CHARACTER:
                return char.class;
            case FLOAT:
                return float.class;
            case DOUBLE:
                return double.class;
            case BOOLEAN:
                return boolean.class;
            case BYTE:
                return byte.class;
            case STRING:
                return String.class;
            default:
                throw new RuntimeException(String.format(
                        "Currently we do not support the class %s", primitive.getName()));
        }
    }

    /**
     * Get boxed version class of primitive type
     * @param primitive - Enum of primitive
     * @return - Class of boxed primitive type
     */
    @SuppressWarnings("rawtypes")
    public static Class getPrimitiveBoxedClass(Primitive primitive) {
        switch (primitive) {
            case SHORT:
                return Short.class;
            case INTEGER:
                return Integer.class;
            case LONG:
                return Long.class;
            case CHARACTER:
                return Character.class;
            case FLOAT:
                return Float.class;
            case DOUBLE:
                return Double.class;
            case BOOLEAN:
                return Boolean.class;
            case BYTE:
                return Byte.class;
            case STRING:
            case CHAR_SEQUENCE:
                return String.class;
            default:
                throw new RuntimeException(String.format(
                        "Currently we do not support the class %s", primitive.getName()));
        }
    }

    /**
     * Get the boxed name of the primitive enum.
     * @param primitive - Type of primitive
     * @return - Boxed class name of the primitive. eg. int -> Integer
     */
    public static String getBoxedName(Primitive primitive) {
        return getPrimitiveBoxedClass(primitive).getSimpleName();
    }

    public static String getBoxedFullName(Primitive primitive) {
        return getPrimitiveBoxedClass(primitive).getName();
    }

    public static String getUnboxedName(Primitive primitive) {
        return getPrimitiveClass(primitive).getSimpleName();
    }

    /***
     * @param type - Name of primitive
     * @return - True if primitive is boxed
     */
    public static boolean isBoxed(String type) {
        return Character.isUpperCase(type.charAt(0));
    }

    /***
     * @param type - Type of primitive
     * @return - True if primitive is boxed
     */
    @SuppressWarnings("rawtypes")
    public static boolean isBoxed(Class type) {
        return isBoxed(type.getSimpleName());
    }

    /**
     * CHeck if the return type is of `void` type
     * @param retType - Return type
     * @return - True if return type is void
     */
    public static boolean isVoid(String retType) {
        return retType != null && VOIDS.contains(retType);
    }
    
}
