package edu.ncsu.arguments;

import com.google.gson.*;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.helpers.FileHandler;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.executors.helpers.ParameterNotFoundException;
import edu.ncsu.executors.helpers.ReflectionHelper;
import edu.ncsu.executors.models.Primitive;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.ISystemClassStore;
import edu.ncsu.utils.JDKUtils;

import java.lang.reflect.*;
import java.util.*;
import java.util.logging.Logger;

@SuppressWarnings("rawtypes")
public class ObjectTypeArguments {

    private final static Logger LOGGER = Logger.getLogger(ObjectTypeArguments.class.getName());

    public static ISystemClassStore SYSTEM_CLASS_STORE = BaseStorage.loadSystemClassStore(ProjectConfig.DATASET);

    public final static String OBJECT = "Object";

    public final static String OBJECT_REFERENCE = "java.lang.Object";

    public final static Gson GSON = new GsonBuilder().serializeSpecialFloatingPointValues().create();

    public final static List<Class> UNSUPPORTED_CLASSES = new ArrayList<>();

    static {
        UNSUPPORTED_CLASSES.add(Throwable.class);
        UNSUPPORTED_CLASSES.add(Runnable.class);
    }

    public static Class getValidClass(String classKey) {
        Class clazz = PackageManager.findGeneratedClass(classKey);
        if (clazz == null)
            clazz = PackageManager.findClass(classKey);
        if (clazz != null && isValidClass(clazz, new HashSet<>()))
            return clazz;
        return null;
    }

    public static JsonObject getValidClassAsJson(Class clazz) {
        if (!isSavedSystemClass(clazz)) {
            return saveClass(clazz, new HashSet<>());
        } else if (!isValidSystemClass(clazz)) {
            return null;
        }
        return SYSTEM_CLASS_STORE.loadClass(ProjectConfig.PROJECT_NAME, ReflectionHelper.makeKey(clazz));
    }

    public static JsonObject getValidClassAsJson(String classKey) {
        if (!isSavedSystemClass(classKey)) {
            return saveClass(getValidClass(classKey), new HashSet<>());
        } else if (!isValidSystemClass(classKey)) {
            return null;
        }
        return SYSTEM_CLASS_STORE.loadClass(ProjectConfig.PROJECT_NAME, classKey);
    }

    @SuppressWarnings("rawtypes")
    public static boolean isUnsupportedClass(Class clazz) {
        for (Class unsupportedClass: UNSUPPORTED_CLASSES) {
            if (unsupportedClass.isAssignableFrom(clazz))
                return true;
        }
        return false;
    }

    public static boolean isValidSystemClass(Class clazz) {
        if (ReflectionHelper.getPackage(clazz) == null)
            return false;
        return SYSTEM_CLASS_STORE.isValidSystemClass(ProjectConfig.PROJECT_NAME, ReflectionHelper.makeKey(clazz));
    }

    public static boolean isValidSystemClass(String classKey) {
        return SYSTEM_CLASS_STORE.isValidSystemClass(ProjectConfig.PROJECT_NAME, classKey);
    }

    public static boolean isSavedSystemClass(Class clazz) {
        if (ReflectionHelper.getPackage(clazz) == null)
            return false;
        return SYSTEM_CLASS_STORE.isSystemClassValiditySaved(ProjectConfig.PROJECT_NAME, ReflectionHelper.makeKey(clazz));
    }

    public static boolean isSavedSystemClass(String classKey) {
        return SYSTEM_CLASS_STORE.isSystemClassValiditySaved(ProjectConfig.PROJECT_NAME, classKey);
    }

    public static Map<String, String> splitClassKey(String classKey) {
        int dotIndex = classKey.lastIndexOf(".");
        String packageName, className;
        if (dotIndex  == -1) {
            packageName = null;
            className = classKey;
        } else {
            packageName = classKey.substring(0, dotIndex);
            className = classKey.substring(dotIndex + 1);
        }
        Map<String, String> splits = new HashMap<>();
        splits.put("packageName", packageName);
        splits.put("className", className);
        return splits;
    }

    public static Constructor getConstructor(String classKey, String constructorKey) {
        Class clazz = getValidClass(classKey);
        if (clazz == null)
            return null;
        for (Constructor constructor: clazz.getConstructors()) {
            if (getKey(constructor).equals(constructorKey))
                return constructor;
        }
        return null;
    }

    public static boolean isFinalClassObject(String classKey) {
        return classKey != null && classKey.equals(OBJECT_REFERENCE);
    }

    public static JsonObject toJsonObject(Constructor constructor) {
        JsonObject jsonObject = new JsonObject();
        JsonArray argsArray = new JsonArray();
        String[] paramNames = getParameterNames(constructor);
        int paramIndex = 0;
        for (Parameter parameter: constructor.getParameters()) {
            Class paramType = parameter.getType();
            int arrayDimensions = ReflectionHelper.getArrayDimensions(parameter.getType());
            paramType =  ReflectionHelper.getBaseClass(paramType);
            JsonObject paramJson = new JsonObject();
            paramJson.addProperty("type", ReflectionHelper.makeKey(paramType));
            paramJson.addProperty("name", paramNames[paramIndex]);
            paramJson.addProperty("arrayDimensions", arrayDimensions);
            argsArray.add(paramJson);
            paramIndex++;
        }
        jsonObject.addProperty("classKey", getKey(constructor.getDeclaringClass()));
        jsonObject.addProperty("key", getKey(constructor));
        jsonObject.add("parameters", argsArray);
        return jsonObject;
    }

    private static String getKey(Class clazz) {
        String key = ReflectionHelper.makeKey(clazz);
        if (Primitive.isValidType(key)) {
            return Primitive.getPrimitive(key).getName();
        }
        return ReflectionHelper.makeKey(clazz);
    }

    public static String getKey(Constructor constructor) {
        List<String> args = new ArrayList<>();
        for (Parameter parameter: constructor.getParameters()) {
            args.add(parameter.getType().getName());
        }
        return String.format("%s(%s)", constructor.getDeclaringClass().getSimpleName(), String.join(",", args));
    }

    public static List<Constructor> getConstructors(Class clazz, Set<Class> seenClasses) {
        List<Constructor> validConstructors = new ArrayList<>();
        for (Constructor constructor: ReflectionHelper.getConstructors(clazz)) {
            if (isValidConstructor(constructor, seenClasses)) {
                validConstructors.add(constructor);
            }
        }
        return validConstructors;
    }

    public static JsonArray getConstructorsAsJson(String classKey) {
        JsonObject jsonObject = getValidClassAsJson(classKey);
        if (jsonObject == null)
            return null;
        if (!jsonObject.has("constructors"))
            return null;
        return jsonObject.get("constructors").getAsJsonArray();
    }


    public static JsonObject getConstructorAsJson(String classKey, String constructorKey) {
        JsonObject jsonObject = getValidClassAsJson(classKey);
        if (jsonObject == null)
            return null;
        if (!jsonObject.has("constructors"))
            return null;
        for (JsonElement element : jsonObject.getAsJsonArray("constructors")) {
            JsonObject constructor = element.getAsJsonObject();
            if (constructor.get("key").getAsString().equals(constructorKey))
                return constructor;
        }
        return null;
    }

    public static JsonObject getOptimalConstructorAsJson(String classKey) {
        JsonObject jsonObject = getValidClassAsJson(classKey);
        if (jsonObject == null)
            return null;
        if (!jsonObject.has("optimalConstructor"))
            return null;
        return jsonObject.get("optimalConstructor").getAsJsonObject();
    }

    /***
     * Get the constructor with least number of arguments as JSON
     * @param classKey
     * @return
     */
    public static Map<String, Object> getSimplestConstructorAsJson(String classKey) {
        JsonObject jsonObject = getValidClassAsJson(classKey);
        if (jsonObject == null)
            return null;
        if (!jsonObject.has("constructors"))
            return null;
        JsonArray constructorsJsonArray = jsonObject.getAsJsonArray("constructors");
        if (constructorsJsonArray.size() == 0)
            return null;
        JsonObject simplestConstructorJson = null;
        int leastArgsCount = Integer.MAX_VALUE;
        for (JsonElement constructorJsonElement: constructorsJsonArray) {
            JsonObject constructorJson = constructorJsonElement.getAsJsonObject();
            int argsCount = 0;
            if (constructorJson.has("parameters") && constructorJson.getAsJsonArray("parameters").size() > 0) {
                for (JsonElement param: constructorJson.getAsJsonArray("parameters")) {
                    JsonObject parameter = param.getAsJsonObject();
                    String paramKey = parameter.get("type").getAsString();
                    if (Primitive.isValidType(paramKey)) {
                        argsCount += 1;
                    } else if (FileHandler.isInputOutputClass(paramKey)) {
                        argsCount += 1;
                    } else if (isValidSystemClass(paramKey)) {
                        int paramArgsCount = getSimplestConstructorArgsCount(paramKey);
                        if (paramArgsCount == -1)
                            return null;
                        argsCount += paramArgsCount;
                    } else {
                        return null;
                    }
                }
            }
            if (argsCount < leastArgsCount) {
                leastArgsCount = argsCount;
                simplestConstructorJson = constructorJson;
            }
        }
        if (simplestConstructorJson == null)
            return null;
        Map<String, Object> simplestConstructorMap = new HashMap<>();
        simplestConstructorMap.put("constructor", simplestConstructorJson);
        simplestConstructorMap.put("argsCount", leastArgsCount);
        return simplestConstructorMap;
    }

    public static int getSimplestConstructorArgsCount(String classKey) {
        Map<String, Object> constructorMap = getSimplestConstructorAsJson(classKey);
        if (constructorMap == null)
            return -1;
        return (int) constructorMap.get("argsCount");
    }

    private static JsonArray toJsonArray(List<String> list) {
        JsonArray jsonArray = new JsonArray();
        for (String key: list)
            jsonArray.add(key);
        return jsonArray;
    }

    public static JsonObject saveClass(Class clazz, Set<Class> seenClasses) {
        clazz = ReflectionHelper.getBaseClass(clazz);
        if (clazz.isInterface())
            return null;
        if (Primitive.isValidType(clazz.getName()))
            return null;
        if (Modifier.isAbstract(clazz.getModifiers()))
            return null;
        seenClasses.add(clazz);
        String packageName = ReflectionHelper.getPackage(clazz);
        String className = clazz.getSimpleName();
        List<Constructor> validConstructors = getConstructors(clazz, seenClasses);
        boolean isValid = validConstructors.size() > 0;
        JsonObject jsonObject = new JsonObject();
        jsonObject.addProperty("key", getKey(clazz));
        jsonObject.addProperty("project", ProjectConfig.PROJECT_NAME);
        jsonObject.addProperty("packageName", packageName);
        jsonObject.add("enclosingClasses", toJsonArray(ReflectionHelper.getEnclosingClasses(clazz)));
        jsonObject.addProperty("className", className);
        jsonObject.addProperty("isValid", isValid);
        if (validConstructors.size() > 0) {
            JsonArray constructorsJson = new JsonArray();
            JsonObject bestConstructor = null;
            int bestParamCount = 0;
            for (Constructor constructor: validConstructors) {
                JsonObject constructorJson = toJsonObject(constructor);
                constructorsJson.add(constructorJson);
                int paramCount = getConstructorParamCount(constructor);
                constructorJson.addProperty("totalParams", paramCount);
                if (bestConstructor == null || paramCount > bestParamCount) {
                    bestConstructor = constructorJson;
                    bestParamCount = paramCount;
                }
            }
            jsonObject.add("constructors", constructorsJson);
            bestConstructor = bestConstructor.deepCopy();
            bestConstructor.addProperty("totalParams", bestParamCount);
            jsonObject.add("optimalConstructor", bestConstructor);
        }
        SYSTEM_CLASS_STORE.updateSystemClassValidity(ProjectConfig.PROJECT_NAME, ReflectionHelper.makeKey(clazz), isValid);
        if (isValid) {
            JsonArray accessors = getAccessors(clazz);
            JsonArray variables = getVariables(clazz);
            jsonObject.add("accessors", accessors);
            jsonObject.add("variables", variables);
            SYSTEM_CLASS_STORE.saveClass(jsonObject);
            return jsonObject;
        }
        return null;
    }

    public static boolean isValidClassKey(String classKey) {
        if (Primitive.isValidType(classKey))
            return true;
        if (FileHandler.isInputOutputClass(classKey))
            return true;
        return isValidClass(classKey);
    }

    public static boolean isValidClass(Class clazz, Set<Class> seenClasses) {
        clazz = ReflectionHelper.getBaseClass(clazz);
        if (clazz.isInterface())
            return false;
        if (Primitive.isValidType(clazz.getName()))
            return true;
        if (FileHandler.isInputOutputClass(clazz.getName()))
            return true;
        if (Modifier.isAbstract(clazz.getModifiers()))
            return false;
        if (isUnsupportedClass(clazz))
            return false;
        String projectName = ProjectConfig.PROJECT_NAME;
        if (SYSTEM_CLASS_STORE.isSystemClassValiditySaved(projectName, ReflectionHelper.makeKey(clazz)))
            return SYSTEM_CLASS_STORE.isValidSystemClass(projectName, ReflectionHelper.makeKey(clazz));
        seenClasses.add(clazz);
        JsonObject savedJson = saveClass(clazz, seenClasses);
        return savedJson != null;
    }

    public static boolean isValidClass(String classKey) {
        Class clazz = getValidClass(classKey);
        return clazz != null;
    }

    public static int getConstructorParamCount(Constructor constructor) {
        int paramCount = 0;
        for (Parameter parameter: constructor.getParameters()) {
            Class parameterType = parameter.getType();
            while (parameterType.isArray())
                parameterType = parameterType.getComponentType();

            if (Primitive.isValidType(parameterType.getName()))
                paramCount++;
            else if (FileHandler.isInputOutputClass(parameterType.getName()))
                paramCount ++;
            else {
                JsonObject paramTypeObj = getValidClassAsJson(parameterType);
                JsonObject obj = paramTypeObj.get("optimalConstructor").getAsJsonObject();
                paramCount += obj.get("totalParams").getAsInt();
            }
        }
        return paramCount;
    }



    private static boolean isAccessor(Method method) {
        return (method.getName().startsWith("get") || method.getName().equals("is"))
                && isValidClass(method.getReturnType(), new HashSet<>());
    }

    public static JsonObject getMetadataAsJson(Class clazz) {
        JsonObject metadata = new JsonObject();
        int arrayDims = ReflectionHelper.getArrayDimensions(clazz);
        Class retType = ReflectionHelper.getBaseClass(clazz);
        String type = retType.getSimpleName();
        metadata.addProperty("arrayDimensions", arrayDims);
        if (!isValidClass(retType, new HashSet<>()))
            return null;
        if (Primitive.isValidType(type)) {
            metadata.addProperty("primitive", Primitive.getPrimitive(type).getName());
            if (Primitive.isBoxed(type))
                metadata.addProperty("boxed", type);
        } else {
            metadata.addProperty("type", type);
            metadata.addProperty("packageName", ReflectionHelper.getPackage(retType));
        }
        return metadata;
    }

    @SuppressWarnings("unchecked")
    public static JsonArray getAccessors(Class clazz) {
        clazz = ReflectionHelper.getBaseClass(clazz);
        JsonArray accessors = new JsonArray();
        Method[] methods = clazz.getMethods();
        for (Method method: methods) {
            if (Modifier.isPublic(method.getModifiers())
                    && !Modifier.isStatic(method.getModifiers())
                    && !Modifier.isAbstract(method.getModifiers())
                    && method.getParameterTypes().length == 0
                    && isAccessor(method)) {
                JsonObject accessor = getMetadataAsJson(method.getReturnType());
                if (accessor == null)
                    continue;
                accessor.addProperty("name", method.getName());
                accessors.add(accessor);
            }
        }
        try {
            Method toStringMethod = clazz.getDeclaredMethod("toString");
            JsonObject accessor = getMetadataAsJson(toStringMethod.getReturnType());
            if (accessor != null) {
                accessor.addProperty("name", "toString");
                accessors.add(accessor);
            }
        } catch (NoSuchMethodException ignored) {}
        return accessors;
    }

    public static JsonArray getVariables(Class clazz) {
        clazz = ReflectionHelper.getBaseClass(clazz);
        JsonArray variables = new JsonArray();
        Map<String, Field> fields = ReflectionHelper.getFields(clazz);
        fields.forEach(
                (name, field) -> {
                    Class fieldType = field.getType();
                    if (Modifier.isPrivate(field.getModifiers()) || !isValidClass(fieldType, new HashSet<>()) || Modifier.isStatic(field.getModifiers()))
                        return;
                    JsonObject fieldJson = getMetadataAsJson(field.getType());
                    if (fieldJson == null)
                        return;
                    fieldJson.addProperty("name", name);
                    variables.add(fieldJson);
                }
        );
        return variables;
    }

    public static boolean isValidConstructor(Constructor constructor, Set<Class> seenClasses){
        if (!Modifier.isPublic(constructor.getModifiers()))
            return false;
        for (Parameter parameter: constructor.getParameters()) {
            Class parameterType = ReflectionHelper.getBaseClass(parameter.getType());
            if (seenClasses.contains(parameterType))
                return false;
            if (!isValidClass(parameterType, new HashSet<>(seenClasses)))
                return false;
        }
        return true;
    }

    /***
     * Return names of parameters for the method/constructor
     * @param methodOrConstructor - A method or constructor reflection object.
     * @return - Array of strings representing argument
     */
    public static String[] getParameterNames(Executable methodOrConstructor) {
        try {
            return ReflectionHelper.getParameterNamesViaReflection(methodOrConstructor);
        } catch (ParameterNotFoundException e) {
            if (PackageManager.isClassFromJDK(methodOrConstructor.getDeclaringClass())) {
                return JDKUtils.getParameterNames(methodOrConstructor);
            }
            throw new RuntimeException("@COSAL: Currently we support system parameter names only from JDK");
        }
    }

    public static String getEnclosedClassName(String classKey) {
        JsonObject classJson = getValidClassAsJson(classKey);
        if (classJson == null)
            return null;
        List<String> classes = new ArrayList<>();
        if (classJson.has("enclosingClasses")) {
            for (JsonElement enclosingClass: classJson.get("enclosingClasses").getAsJsonArray()) {
                classes.add(enclosingClass.getAsString());
            }
        }
        classes.add(classJson.get("className").getAsString());
        return String.join(".", classes);
    }

    public static boolean areSameObjects(Object one, Object two) {
        if (one == null && two == null)
            return true;
        else if (one == null || two == null)
            return false;
        else if (one.getClass() != two.getClass())
            return false;
        Class clazz = one.getClass();
        int arrayDimensions = ReflectionHelper.getArrayDimensions(clazz);
        if (arrayDimensions == 0) {
            if (Primitive.isPrimitive(clazz)) {
                return one.equals(two);
            } else if (FileHandler.isOutputClass(clazz.getName())) {
                throw new RuntimeException("@COSAL: Why have you not yet implemented output comparison for files??");
            } else if (isValidClass(clazz, new HashSet<>())) {
                JsonObject jsonObject = getValidClassAsJson(clazz);
                if (jsonObject == null)
                    return false;
                JsonArray variables = jsonObject.getAsJsonArray("variables");
                Map<String, Field> fields = ReflectionHelper.getFields(clazz);
                try {
                    for (JsonElement variable: variables) {
                        Field field = fields.get(variable.getAsJsonObject().get("name").getAsString());
                        field.setAccessible(true);
                        Object oneFieldValue = field.get(one);
                        Object twoFieldValue = field.get(two);
                        if (!areSameObjects(oneFieldValue, twoFieldValue))
                            return false;
                    }
                } catch (IllegalAccessException e) {
                    return false;
                }
            } else {
                if (Settings.DEBUG)
                    LOGGER.severe(String.format("We currently do not support the class %s", clazz.getName()));
                return false;
            }
        } else {
            Object[] oneArray = ReflectionHelper.toObjectArray(one);
            Object[] twoArray = ReflectionHelper.toObjectArray(two);
            if (oneArray.length != twoArray.length)
                return false;
            for (int arrayIndex = 0; arrayIndex < oneArray.length; arrayIndex++) {
                if (!areSameObjects(oneArray[arrayIndex], twoArray[arrayIndex]))
                    return false;
            }
        }
        return true;
    }

    public static void test() {
//        Set<Class> classes = new HashSet<>();
//        Integer x = 5;
//        Integer y = 6;
//        classes.add(x.getClass());
//        classes.add(Float.class);
//        classes.add(Integer.class);
//        System.out.println(classes.size());
//        System.out.println(classes.contains(y.getClass()));
        System.out.println(getSimplestConstructorAsJson("CodeJam.Y11R5P1.vot.a$Point"));
//        System.out.println(isValidClass(Exception.class, new HashSet<>()));
//        System.out.println(getValidClass("java.lang", "StringBuilder"));
//        System.out.println(Primitive.isValidType(ReflectionHelper.makeKey(int.class)));
//        System.out.println(clazz.getDeclaringClass());
//        Class clazz = PackageManager.findClass("java.lang", "StringBuilder");
//        Method method = clazz.getDeclaredMethod("toString");
//        System.out.println(method);
//        clazz = PackageManager.findClass("Dummy.area",  "Line");
//        method = clazz.getDeclaredMethod("toString");
//        System.out.println(method);

    }

    public static void main(String[] args) {
        test();
    }

}
