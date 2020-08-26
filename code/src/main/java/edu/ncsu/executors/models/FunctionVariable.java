package edu.ncsu.executors.models;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import edu.ncsu.arguments.ObjectTypeArguments;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.executors.helpers.FileHandler;
import edu.ncsu.executors.helpers.ReflectionHelper;
import org.apache.commons.lang3.ArrayUtils;
import org.apache.commons.lang3.StringUtils;

import java.lang.reflect.*;
import java.util.*;

public class FunctionVariable {

    private String dataset;

    private String name;

    private Primitive primitive;

    private String dataType;

    private String packageName;

    private com.github.javaparser.ast.body.Parameter parameterAST = null;

    private String fullTypeKey = null;

    private int arrayDimensions = 0;

    private boolean isFuzzable = true;

    private boolean isBuiltInType = false;

    private SystemClassConstructor systemClassConstructor = null;

    private List<String> genericTypes;

    private FunctionVariable(){}

    /**
     * Create a function variable
     * @param dataset - Name of dataset
     * @param parameterType - Reflection parameter
     * @param parameterAST - AST of parameter
     */
    public FunctionVariable(String dataset, Type parameterType, com.github.javaparser.ast.body.Parameter parameterAST) {
        this.dataset = dataset;
        this.parameterAST = parameterAST;
        this.name = parameterAST.getNameAsString();
        setType(parameterType);
    }

    /**
     * Create a function variable
     * @param dataset - Name of dataset
     * @param returnType - Class of variable type
     */
    @SuppressWarnings("rawtypes")
    public FunctionVariable(String dataset, Type returnType) {
        this.dataset = dataset;
        setType(returnType);
    }

    /***
     * Create a function variable from metadata
     * @param varMetadata - JSON representation of variable's metadata
     */
    @SuppressWarnings("rawtypes")
    public FunctionVariable(JsonObject varMetadata) {
        this.dataset = ProjectConfig.DATASET;
        if (varMetadata.has("name")) {
            this.name = varMetadata.get("name").getAsString();
        }
        this.arrayDimensions = varMetadata.get("arrayDimensions").getAsInt();
        if (varMetadata.has("primitive")) {
            Primitive varPrimitive = Primitive.getPrimitive(varMetadata.get("primitive").getAsString());
            this.primitive = varPrimitive;
            Class primitiveClass;
            if (varMetadata.has("isBoxedPrimitive") && varMetadata.get("isBoxedPrimitive").getAsBoolean()) {
                this.dataType = Primitive.getBoxedName(varPrimitive);
                this.packageName = "java.lang";
                primitiveClass = Primitive.getPrimitiveBoxedClass(varPrimitive);
            } else {
                primitiveClass = Primitive.getPrimitiveClass(varPrimitive);
            }
            fullTypeKey = ReflectionHelper.makeKey(primitiveClass);
        } else if (varMetadata.has("isSystemClass") && varMetadata.get("isSystemClass").getAsBoolean()) {
            String classKey = varMetadata.get("classKey").getAsString();
            this.fullTypeKey = classKey;
            Class clazz = ObjectTypeArguments.getValidClass(classKey);
            if (clazz == null)
                throw new RuntimeException(String.format("No class found for type : %s", varMetadata.get("classKey").getAsString()));
            this.dataType = clazz.getSimpleName();
            this.packageName = ReflectionHelper.getPackage(clazz);
            String constructorKey = varMetadata.get("key").getAsString();
            JsonObject constructorJson = ObjectTypeArguments.getConstructorAsJson(classKey, constructorKey);
            if (constructorJson == null)
                throw new RuntimeException(String.format("Failed to fetch constructor arg for constructor key: %s", constructorKey));
            List<FunctionVariable> constructorArgs = new ArrayList<>();
            if (varMetadata.has("argsMetadata")) {
                for (JsonElement element : varMetadata.get("argsMetadata").getAsJsonArray()) {
                    JsonObject argMetadata = element.getAsJsonObject();
                    FunctionVariable constructorArg = new FunctionVariable(argMetadata);
                    constructorArgs.add(constructorArg);
                }
            }
            this.systemClassConstructor = new SystemClassConstructor(constructorJson, constructorArgs);
        } else if (varMetadata.has("fileType")) {
            this.isBuiltInType = true;
            this.fullTypeKey = varMetadata.get("key").getAsString();
            this.dataType = varMetadata.get("dataType").getAsString();
            this.packageName = varMetadata.get("packageName").getAsString();
        } else {
            throw new RuntimeException(String.format("Failed to create function variable for key: %s", varMetadata.get("key").getAsString()));
        }
    }

    /***
     * Create a function variable from metadata and instance of systemn class constructor
     * @param varJson - JSON representation of variable's metadata
     * @param systemClassConstructor - Instance of system class constructor
     */
    @SuppressWarnings("rawtypes")
    public FunctionVariable(JsonObject varJson, SystemClassConstructor systemClassConstructor) {
        this.dataset = ProjectConfig.DATASET;
        this.name = varJson.get("name").getAsString();
        this.arrayDimensions = varJson.get("arrayDimensions").getAsInt();
        String type = varJson.get("type").getAsString();
        if (Primitive.isValidType(type)) {
            Primitive varPrimitive = Primitive.getPrimitive(type);
            Class primitiveClass;
            if (type.startsWith("java.lang")) {
                this.dataType = type.substring(10); // Index of java.lang"."
                this.packageName = "java.lang";
                primitiveClass = Primitive.getPrimitiveBoxedClass(varPrimitive);
            } else {
                primitiveClass = Primitive.getPrimitiveClass(varPrimitive);
            }
            this.primitive = varPrimitive;
            this.fullTypeKey = ReflectionHelper.makeKey(primitiveClass);
        } else if (FileHandler.isInputOutputClass(type)) {
            this.isBuiltInType = true;
            Map<String, String> splits = ObjectTypeArguments.splitClassKey(type);
            this.packageName = splits.get("packageName");
            this.dataType = splits.get("className");
            this.fullTypeKey = type;
        } else {
            Class clazz = ObjectTypeArguments.getValidClass(type);
            if (clazz == null)
                throw new RuntimeException(String.format("No class found for type : %s", type));
            this.dataType = clazz.getSimpleName();
            this.packageName = ReflectionHelper.getPackage(clazz);
            this.fullTypeKey = ReflectionHelper.makeKey(clazz);
            this.systemClassConstructor = systemClassConstructor;
        }
    }

    /**
     * Clone a function variable. Used while permutation
     * @param functionVariable - Instance of FunctionVariable to clone
     * @return - Cloned FunctionVariable
     */
    public static FunctionVariable clone(FunctionVariable functionVariable) {
        FunctionVariable newFunctionVariable = new FunctionVariable();
        newFunctionVariable.dataset = functionVariable.dataset;
        newFunctionVariable.name = functionVariable.name;
        newFunctionVariable.primitive = functionVariable.primitive;
        newFunctionVariable.dataType = functionVariable.dataType;
        newFunctionVariable.packageName = functionVariable.packageName;
        newFunctionVariable.parameterAST = functionVariable.parameterAST;
        newFunctionVariable.arrayDimensions = functionVariable.arrayDimensions;
        newFunctionVariable.isFuzzable = functionVariable.isFuzzable;
        newFunctionVariable.isBuiltInType = functionVariable.isBuiltInType;
        newFunctionVariable.systemClassConstructor = functionVariable.systemClassConstructor;
        newFunctionVariable.fullTypeKey = functionVariable.fullTypeKey;
        return newFunctionVariable;
    }

    /**
     * Set type of of function variable from a Class object
     * @param type - Class to infer type from
     */
    @SuppressWarnings("rawtypes")
    private void setType(Type type) {
        Class clazz;
        if (type instanceof ParameterizedType) {
            this.genericTypes = new ArrayList<>();
            ParameterizedType parameterizedType = (ParameterizedType) type;
            for (Type parameterizedArgType: parameterizedType.getActualTypeArguments()) {
                if (parameterizedArgType instanceof Class) {
                    String paramKey = ReflectionHelper.makeKey((Class) parameterizedArgType);
                    if (!ObjectTypeArguments.isValidClassKey(paramKey))
                        this.isFuzzable = false;
                    this.genericTypes.add(paramKey);
                } else {
                    this.isFuzzable = false;
                }
            }
            clazz = (Class) parameterizedType.getRawType();
        } else {
            clazz = (Class) type;
        }
        this.arrayDimensions = ReflectionHelper.getArrayDimensions(clazz);
        Class baseType = ReflectionHelper.getBaseClass(clazz);
        String thisFullTypeKey = ReflectionHelper.makeKey(baseType);
        if (Primitive.isValidType(baseType)) {
            this.primitive = Primitive.getPrimitive(baseType);
            if (Primitive.isBoxed(baseType)) {
                this.dataType = baseType.getSimpleName();
            }
        } else {
            this.dataType = baseType.getSimpleName();
            this.packageName = ReflectionHelper.getPackage(baseType);
            this.isBuiltInType = FileHandler.isInputOutputClass(thisFullTypeKey);
            if (!this.isBuiltInType) {
                this.isFuzzable = ObjectTypeArguments.isValidClass(thisFullTypeKey);
            }
        }
        this.fullTypeKey = thisFullTypeKey;
    }

    /**
     * @return - dataset
     */
    public String getDataset() {
        return dataset;
    }

    /**
     * @return - Name of the variable
     */
    public String getName() {
        return name;
    }

    /***
     * Set name of the variable
     * @param name - Name of the variable
     */
    public void setName(String name) {
        this.name = name;
    }

    /***
     * @return - Primitive ENUM if the variable is a primitive
     */
    public Primitive getPrimitive() {
        return primitive;
    }

    /***
     * @param primitive - Set the primitive
     */
    public void setPrimitive(Primitive primitive) {
        this.primitive = primitive;
    }

    /***
     * @return - dataType of the variable
     */
    public String getDataType() {
        return dataType;
    }

    /**
     * @return - array dimensions of variable
     */
    public int getArrayDimensions() {
        return arrayDimensions;
    }

    /**
     * Set array dimensions of variable
     * @param arrayDimensions - array dimensions of variable
     */
    public void setArrayDimensions(int arrayDimensions) {
        this.arrayDimensions = arrayDimensions;
    }

    /**
     * @return - True if the variable is fuzzable
     */
    boolean isFuzzable() {
        return isFuzzable;
    }

    /**
      * @return - Return true if its a File Input/Output type
     */
    public boolean isBuiltInType() {
        return isBuiltInType;
    }

    /**
     * @return - Name of the package
     */
    public String getPackageName() {
        return packageName;
    }

    /**
     * @return - SystemClassConstructor object if it is not a primitive
     */
    public SystemClassConstructor getSystemClassConstructor() {
        return systemClassConstructor;
    }

//    /**
//     * @return - ClassKey if is a system class.
//     */
//    public String getSystemClassKey() {
//        if (systemClassConstructor == null)
//            return null;
//        return systemClassConstructor.getJsonObject().get("classKey").getAsString();
//    }

    /**
     * Set SystemClassConstructor for the variable
     * @param systemClassConstructor - Instance of SystemClassConstructor
     */
    public void setSystemClassConstructor(SystemClassConstructor systemClassConstructor) {
        this.systemClassConstructor = systemClassConstructor;
    }

    /**
     * Represent as a string
     * @return - String representation of FunctionVariable
     */
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        if (isFuzzable) {
            sb.append("+");
        } else {
            sb.append("-");
        }
        if (primitive != null) {
            sb.append(primitive.getName());
        } else if (dataType != null){
            if (packageName != null) {
                sb.append(getFullTypeKey());
            } else {
                sb.append(dataType);
            }

        }
        if (arrayDimensions > 0) {
            for (int i=0; i < arrayDimensions; i++)
                sb.append("[]");
        }
        if (name != null) {
            sb.append(" ").append(name);
        }
        return sb.toString();
    }

    /**
     * @return - String representation of type.
     */
    public String getFullTypeKey() {
        if (fullTypeKey != null)
            return fullTypeKey;
        if (primitive != null) {
            if (primitive.equals(Primitive.STRING) || dataType != null) {
                fullTypeKey = Primitive.getBoxedName(primitive);
                return fullTypeKey;
            }
            fullTypeKey = Primitive.getPrimitiveClass(primitive).getSimpleName();
            return fullTypeKey;
        } else if (systemClassConstructor != null) {
            String classKey = systemClassConstructor.getClassKey();
            if (classKey != null) {
                fullTypeKey = classKey;
                return fullTypeKey;
            }
        }
        if (packageName != null) {
            fullTypeKey = String.format("%s.%s", packageName, dataType);
        } else {
            fullTypeKey = dataType;
        }
        return fullTypeKey;
    }

    /**
     * @return - Convert function variable to a string representation of the variable
     */
    public String toFunctionParameter() {
        if (this.parameterAST != null) {
            return this.parameterAST.toString();
        } else {
            StringBuilder sb = new StringBuilder();
            String dt = null;
            if (primitive != null) {
                if (primitive.equals(Primitive.STRING) || dataType != null) {
                    dt = Primitive.getBoxedName(primitive);
                } else {
                    dt = Primitive.getPrimitiveClass(primitive).getSimpleName();
                }
            }  else if (systemClassConstructor != null) {
                dt = ObjectTypeArguments.getEnclosedClassName(systemClassConstructor.getClassKey());
            }
            if (dt == null) {
                dt = dataType;
            }
            sb.append(dt);
            if (arrayDimensions > 0) {
                for (int i=0; i < arrayDimensions; i++)
                    sb.append("[]");
            }
            sb.append(" ").append(getName());
            return sb.toString();
        }
    }

    public boolean isUnboxedPrimitive() {
        return primitive != null && StringUtils.isEmpty(dataType);
    }

    @SuppressWarnings("rawtypes")
    private static Object invokeConstructor(Constructor constructor, List<Object> params) {
        try {
            constructor.setAccessible(true);
            return constructor.newInstance(params.toArray());
        } catch (InstantiationException e) {
            throw new RuntimeException(String.format("InstantiationException: %s", e.getMessage()), e);
        } catch (IllegalAccessException e) {
            throw new RuntimeException(String.format("IllegalAccessException: %s", e.getMessage()), e);
        } catch (InvocationTargetException e) {
            throw new RuntimeException(String.format("InvocationTargetException: %s", e.getMessage()), e.getTargetException());
        }
    }

    @SuppressWarnings("rawtypes")
    public Object convertToFunctionArgument(String argName, Map<String, Map<String, Object>> nameArgTypeMap, int arrayDimensions, int funcUUID, int argSetIndex) {
        if (arrayDimensions == 0) {
            if (primitive != null) {
                Object argVal = nameArgTypeMap.get(argName).get("arg");
                Object converted = Primitive.convertToArgument(primitive, argVal.toString());
                return converted;
//                if (isUnboxedPrimitive()) {
//                    Class primitiveClass = Primitive.getPrimitiveClass(primitive);
//                    return primitiveClass.cast(converted);
//                } else {
//                    return converted;
//                }
            } else if (systemClassConstructor != null) {
                String classKey = systemClassConstructor.getJsonObject().get("classKey").getAsString();
                if (ObjectTypeArguments.isFinalClassObject(classKey)) {
                    Object argVal = nameArgTypeMap.get(argName).get("arg");
                    return Primitive.convertToArgument(argVal.toString());
                } else {
                    Constructor constructorClass = ObjectTypeArguments.getConstructor(classKey, systemClassConstructor.getJsonObject().get("key").getAsString());
                    assert constructorClass != null;
                    SystemClassConstructor systemClassConstructor = this.getSystemClassConstructor();
                    List<Object> constructorArgVals = new ArrayList<>();
                    if (systemClassConstructor.getArguments() != null && systemClassConstructor.getArguments().size() >0 ){
                        for (FunctionVariable constructorParam: systemClassConstructor.getArguments()) {
                            constructorArgVals.add(constructorParam.convertToFunctionArgument(
                                    String.format("%s.%s", argName, constructorParam.getName()),
                                    nameArgTypeMap,
                                    constructorParam.getArrayDimensions(),
                                    funcUUID,
                                    argSetIndex));
                        }
                    }
                    try {
                        return FunctionVariable.invokeConstructor(constructorClass, constructorArgVals);
                    } catch (RuntimeException e) {
                        return null;
                    }
                }
            } else if (isBuiltInType) {
                String key = getFullTypeKey();
                Object argVal = nameArgTypeMap.get(argName).get("arg");
                if (FileHandler.isInputClass(key)) {
                    return FileHandler.convertFileInput(key, argVal.toString());
                } else if (FileHandler.isOutputClass(key)) {
                    return FileHandler.convertFileOutput(key, funcUUID, argSetIndex);
                }
                throw new RuntimeException(String.format("We do not support %s", key));
            } else {
                throw new RuntimeException(String.format("This should be saved as a systemClass. Check DB for key: %s", dataType));
            }
        } else {
            JsonArray arrayArg = (JsonArray) nameArgTypeMap.get(argName).get("arg");
            List vals = new ArrayList();
            for (JsonElement argVal : arrayArg) {
                vals.add(convertToFunctionArgument((JsonArray) argVal, arrayDimensions - 1, funcUUID, argSetIndex));
            }
            if (isUnboxedPrimitive()) {
                Class boxedArrayClass = ReflectionHelper.makeArrayClass(Primitive.getPrimitiveBoxedClass(primitive), arrayDimensions);
                Object casted = ArrayUtils.toPrimitive(Arrays.copyOf(vals.toArray(), vals.size(), boxedArrayClass));
                return casted;
            } else {
                return ReflectionHelper.toObjectArray(vals.toArray());
//                return Arrays.copyOf(vals.toArray(), vals.size());
            }
//            Class baseClass = getClassInstantiation();
//            Class arrayClass = Array.newInstance(baseClass, vals.size()).getClass();
//            return Arrays.copyOf(vals.toArray(), vals.size(), arrayClass);
        }
    }

    @SuppressWarnings("rawtypes")
    private Object convertToFunctionArgument(JsonArray arg, int arrayDimensions, int funcUUID, int argSetIndex) {
        if (arrayDimensions == 0) {
            if (primitive != null) {
                Object argVal = arg.get(0);
                arg.remove(0);
                return Primitive.convertToArgument(primitive, argVal.toString());
            } else if (systemClassConstructor != null) {
                String classKey = systemClassConstructor.getJsonObject().get("classKey").getAsString();
                if (ObjectTypeArguments.isFinalClassObject(classKey)) {
                    Object argVal = arg.get(0);
                    arg.remove(0);
                    return Primitive.convertToArgument(argVal.toString());
                } else {
                    Constructor constructorClass = ObjectTypeArguments.getConstructor(classKey, systemClassConstructor.getJsonObject().get("key").getAsString());
                    assert constructorClass != null;
                    SystemClassConstructor systemClassConstructor = this.getSystemClassConstructor();
                    List<Object> constructorArgVals = new ArrayList<>();
                    if (systemClassConstructor.getArguments() != null && systemClassConstructor.getArguments().size() >0 ){
                        for (FunctionVariable constructorParam: systemClassConstructor.getArguments()) {
                            constructorArgVals.add(constructorParam.convertToFunctionArgument(
                                    arg,
                                    constructorParam.getArrayDimensions(),
                                    funcUUID,
                                    argSetIndex));
                        }
                    }
                    try {
                        return FunctionVariable.invokeConstructor(constructorClass, constructorArgVals);
                    } catch (RuntimeException e) {
                        return null;
                    }

                }
            } else if (isBuiltInType) {
                String key = getFullTypeKey();
                Object argVal = arg.get(0);
                arg.remove(0);
                if (FileHandler.isInputClass(key)) {
                    return FileHandler.convertFileInput(key, argVal.toString());
                } else if (FileHandler.isOutputClass(key)) {
                    return FileHandler.convertFileOutput(key, funcUUID, argSetIndex);
                }
                throw new RuntimeException(String.format("We do not support %s", key));
            } else {
                throw new RuntimeException(String.format("This should be saved as a systemClass. Check DB for key: %s", dataType));
            }
        } else {
            JsonElement arrayArg = arg.get(0);
            arg.remove(0);
            List<Object> vals = new ArrayList<>();
            for (JsonElement argVal: arrayArg.getAsJsonArray()) {
                try {
                    if (argVal.isJsonArray()) {
                        vals.add(convertToFunctionArgument(argVal.getAsJsonArray(), arrayDimensions - 1, funcUUID, argSetIndex));
                    } else {
                        JsonArray argValArray = new JsonArray();
                        argValArray.add(argVal);
                        vals.add(convertToFunctionArgument(argValArray, arrayDimensions - 1, funcUUID, argSetIndex));
                    }
                } catch (Exception e) {
                    System.out.println(argVal);
                    throw new RuntimeException(e);
                }

            }
            if (isUnboxedPrimitive()) {
                Class boxedArrayClass = ReflectionHelper.makeArrayClass(Primitive.getPrimitiveBoxedClass(primitive), arrayDimensions);
                Object casted = ArrayUtils.toPrimitive(Arrays.copyOf(vals.toArray(), vals.size(), boxedArrayClass));
                return casted;
            } else {
                return ReflectionHelper.toObjectArray(vals.toArray());
            }
        }
    }

    public JsonObject getMetadataAsJson() {
        JsonObject jsonObject = new JsonObject();
        jsonObject.addProperty("arrayDimensions", arrayDimensions);
        if (this.name != null)
            jsonObject.addProperty("name", name);
        if (systemClassConstructor != null) {
            jsonObject.addProperty("isSystemClass", true);
            JsonObject constructorJson = systemClassConstructor.makeMetadata();
            jsonObject.addProperty("classKey", constructorJson.get("classKey").getAsString());
            jsonObject.addProperty("key", constructorJson.get("key").getAsString());
            jsonObject.add("argsMetadata", constructorJson.get("argsMetadata"));
        } else {
            if (this.primitive != null) {
//                jsonObject.addProperty("key", primitive.getName());
                jsonObject.addProperty("key", primitive.getFamily().getName());
                jsonObject.addProperty("primitive", getPrimitive().getName());
                if (this.dataType != null) {
                    jsonObject.addProperty("isBoxedPrimitive", true);
                }
            } else {
                String key = getFullTypeKey();
                if (FileHandler.isInputClass(key)) {
                    jsonObject.addProperty("fileType", FileHandler.FILE_INPUT_TYPE);
                } else if  (FileHandler.isOutputClass(key)) {
                    jsonObject.addProperty("fileType", FileHandler.FILE_OUTPUT_TYPE);
                }
                jsonObject.addProperty("key", key);
                jsonObject.addProperty("dataType", this.dataType);
                jsonObject.addProperty("packageName", this.packageName);
            }
        }
        return jsonObject;
    }

    public static class FunctionArgComparator implements Comparator<FunctionVariable> {
        @Override
        public int compare(FunctionVariable o1, FunctionVariable o2) {
            if (o1.primitive != null && o2.primitive != null) {
                if (o1.primitive.getIndex() == o2.primitive.getIndex()) {
                    return Integer.compare(o1.getArrayDimensions(), o2.getArrayDimensions());
                } else {
                    return Integer.compare(o1.primitive.getIndex(), o2.primitive.getIndex());
                }
            } else if (o1.primitive != null) {
                return -1;
            } else if (o2.primitive != null) {
                return 1;
            } else {
                String o1Type = o1.getDataType();
                String o2Type = o2.getDataType();
                if (o1Type.equals(o2Type)) {
                    return Integer.compare(o1.getArrayDimensions(), o2.getArrayDimensions());
                } else {
                    return o1Type.compareTo(o2Type);
                }
            }
        }
    }

    public static void main(String[] args) {
        List<Object> list = new ArrayList<>();

        Object[] objects = new Integer[5];
        for (int i=0; i<5; i++) {
            objects[i] = i * 2;
            list.add(objects[i]);
        }
        Class boxedArrayClass = ReflectionHelper.makeArrayClass(Primitive.getPrimitiveBoxedClass(Primitive.INTEGER), 1);
        System.out.println(Arrays.toString(objects));
        System.out.println(ArrayUtils.toPrimitive(Arrays.copyOf(list.toArray(), list.size(), boxedArrayClass)).getClass());
    }

}
