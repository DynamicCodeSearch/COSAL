package edu.ncsu.executors.models;

import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.comments.Comment;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonPrimitive;
import edu.ncsu.arguments.ObjectTypeArguments;
import edu.ncsu.executors.helpers.FileHandler;
import edu.ncsu.executors.helpers.ReflectionHelper;
import edu.ncsu.config.hyperparameters.HyperParameters;
import org.apache.commons.lang3.StringUtils;

import java.lang.reflect.*;
import java.util.*;

public class Function {

    private String uuid;

    private String dataset;

    private String filePath;

    private String baseFilePath;

    private Method method;

    private MethodDeclaration ast;

    private List<Integer> linesTouched;

    private List<Integer> span;

    private List<FunctionVariable> arguments;

    private FunctionVariable returnVariable;

    private boolean isFuzzable = true;

    private String argsKey = null;

    private JsonObject metadata = null;

    public String getPackageName() {
        return ReflectionHelper.getPackage(method.getDeclaringClass());
    }

    public String getClassName() {
        return method.getDeclaringClass().getSimpleName();
    }

    public String getName() {
        if (uuid != null)
            return uuid;
        return method.getName();
    }

    public String getFunctionBody() {
        return ast.getBody().toString();
    }

    public Method getMethod() {
        return method;
    }

    public MethodDeclaration getAst() {
        return ast;
    }


    public List<FunctionVariable> getArguments() {
        return arguments;
    }

    public FunctionVariable getReturnVariable() {
        return returnVariable;
    }

    public boolean isFuzzable() {
        return isFuzzable;
    }

    public List<Integer> getLinesTouched() {
        return linesTouched;
    }

    public List<Integer> getSpan() {
        return span;
    }

    public JsonObject getMetadata() {
        return this.metadata;
    }

    public void setArguments(List<FunctionVariable> arguments) {
        this.arguments = arguments;
    }

    /***
     * Initialize Function Object
     * @param dataset - Dataset of the function
     * @param method - Instance of java reflection Method
     * @param ast - AST of the method from JavaParser
     * @param filePath - Path to the file containing the function
     */
    public Function(String dataset, Method method, MethodDeclaration ast, String filePath) {
        this.dataset = dataset;
        this.method = method;
        this.method.setAccessible(true);
        this.ast = ast;
        this.filePath = filePath;
        arguments = new ArrayList<>();
        Type[] paramTypes = method.getGenericParameterTypes();
        assert paramTypes.length == ast.getParameters().size();
        int paramIndex = 0;
        for (Type paramType: paramTypes) {
            FunctionVariable variable = new FunctionVariable(this.dataset, paramType, ast.getParameter(paramIndex));
            if (!variable.isFuzzable())
                this.isFuzzable = false;
            arguments.add(variable);
            paramIndex++;
        }
        try {
            returnVariable = new FunctionVariable(this.dataset, method.getGenericReturnType());
            if (!returnVariable.isFuzzable()
                    || FileHandler.isInputClass(returnVariable.getFullTypeKey())
                    || hasMultipleWriteArguments())
                this.isFuzzable = false;
        } catch (RuntimeException e) {
            returnVariable = null;
            this.isFuzzable = false;
        }
        processComments();
    }

    private Function(){}

    public Function clone() {
        Function function = new Function();
        function.uuid = this.uuid;
        function.dataset = this.dataset;
        function.filePath = this.filePath;
        function.baseFilePath = this.baseFilePath;
        function.method = this.method;
        function.ast = this.ast;
        function.linesTouched = this.linesTouched;
        function.span = this.span;
        function.arguments = this.arguments;
        function.returnVariable = this.returnVariable;
        function.isFuzzable = this.isFuzzable;
        function.argsKey = this.argsKey;
        function.metadata = this.metadata;
        return function;
    }


    public void setUuid(String uuid) {
        this.uuid = uuid;
    }

    /**
     * Set the metadata for function. Also update systemclass constructors for the arguments.
     * @param metadata - JsonObject representing metadata
     */
    public void setMetadata(JsonObject metadata) {
        this.metadata = metadata;
        JsonElement argsMetadata = metadata.get("argsMetadata");
        if (argsMetadata != null) {
            int argIndex = 0;
            for (JsonElement argMetadata: (JsonArray) argsMetadata) {
                JsonObject argMeta = (JsonObject) argMetadata;
                FunctionVariable generatedArgMeta = new FunctionVariable(argMeta);
                arguments.get(argIndex).setSystemClassConstructor(generatedArgMeta.getSystemClassConstructor());
                argIndex += 1;
            }
        }
    }

    /**
     * Check if the function args are valid fuzzable objects
     * @return - True if all arguments are valid
     */
    public boolean isValidArgs() {
        for (FunctionVariable variable: arguments) {
            if (!variable.isFuzzable())
                return false;
        }
        return true;
    }

    /**
     * Return argument key for the function
     * @return - String representation of arguments which is used as a key.
     */
    public String getArgumentsKey() {
        if (this.argsKey == null) {
            if (this.getMetadata() == null)
                return null;
            this.argsKey = makeArgumentsKey(Function.decodeArgsPermutation(this.getMetadata().getAsJsonObject("argsPermutation")));
        }
        return this.argsKey;
    }

    /***
     * Helper function to make arguments key from a map of argsPermutation
     * @param argsPermutation - Map of argtypes and names.
     * @return - String representation fo argnames
     */
    public static String makeArgumentsKey(Map<String, List<String>> argsPermutation) {
        List<String> keys = new ArrayList<>(argsPermutation.keySet());
        Collections.sort(keys);
        List<String> argKeys = new ArrayList<>();
        for (String key: keys) {
            argKeys.add(String.format("%s##%d", key, argsPermutation.get(key).size()));
        }
        return String.join(",", argKeys);

    }

    /***
     * Skip this function if the number of arguments are more than the number of hyper parameters
     * @return - True if the function should be completed
     */
    public boolean shouldBeSkipped() {
        // TODO: Change this from arguments size to total expanded params. Check the totalParams property from the jsonObject in systemClassConstructor
        return arguments.size() > HyperParameters.MAX_NUM_ARGS;
    }

    /***
     * Helper function to return true if it has multiple write file arguments
     * @return - True if the function has multiple write file arguments
     */
    private boolean hasMultipleWriteArguments() {
        int n_write_args = 0;
        for (FunctionVariable arg: arguments) {
            if (FileHandler.isOutputClass(arg.getFullTypeKey()))
                n_write_args += 1;
        }
        return n_write_args > 1;
    }

    /**
     * Helper function to return a UUID for the function
     * @return - Hashcode for the function
     */
    public int getUUID() {
        return System.identityHashCode(this);
    }

    /***
     * Process embedded comments from the function body. Useful for generated function.
     * Updates the accessors baseFilepath, linesTouched, and span.
     */
    private void processComments() {
        List<Comment> comments = ast.getAllContainedComments();
        if (comments == null || comments.size() == 0)
            return;
        String comment = comments.get(0).getContent();
        comment = comment.replaceAll("\\s", "").replace("*", "");
        for (String m : comment.split(";")) {
            String[] mSplits = m.split(":");
            switch (mSplits[0]) {
                case "source":
                    this.baseFilePath = mSplits[1];
                    break;
                case "lines":
                    this.linesTouched = new ArrayList<>();
                    for (String lineStr : mSplits[1].split(","))
                        this.linesTouched.add(Integer.parseInt(lineStr));
                    Collections.sort(this.linesTouched);
                    break;
                case "start_end":
                    this.span = new ArrayList<>();
                    for (String lineStr : mSplits[1].split(","))
                        this.span.add(Integer.parseInt(lineStr));
                    Collections.sort(this.span);
                    break;
            }
        }
    }

    /***
     * Construct arguments Key based on the names of a list of function variables
     * @param args - List of FunctionVariable
     * @return - String representing a key
     */
    public static String constructArgumentNamesKey(List<FunctionVariable> args) {
        List<String> argNames = new ArrayList<>();
        for (FunctionVariable argument: args) {
            argNames.add(argument.getName());
        }
        if (argNames.size() == 0)
            return null;
        return StringUtils.join(argNames, ",");
    }

    /***
     * Convert a JsonObject of arg values to the corresponding function variable values.
     * @param args - JsonObject of a generated arg for the function
     * @param argIndex - Index of the arg. Used in write file creation to access.
     * @return - List of converted args which can be used for execution.
     */
    public List<Object> convertToFunctionArguments(Object args, int argIndex) {
        JsonObject argsJson = (JsonObject) args;
        JsonObject funcMetadata = getMetadata();
        Map<String, List<String>> argsPermutation = Function.decodeArgsPermutation(funcMetadata.getAsJsonObject("argsPermutation"));
        Map<String, Map<String, Object>> nameArgTypeMap = new HashMap<>();
        for (String typeKey: argsPermutation.keySet()) {
            for (String argName: argsPermutation.get(typeKey)) {
                Map<String, Object> argTypeMap = new HashMap<>();
                argTypeMap.put("type", typeKey);
                argTypeMap.put("arg", argsJson.getAsJsonArray(typeKey).remove(0));
                nameArgTypeMap.put(argName, argTypeMap);
            }
        }
        int funcUUID = getUUID();
        List<Object> funcArgs = new ArrayList<>();
        for (FunctionVariable arg: arguments) {
            funcArgs.add(arg.convertToFunctionArgument(arg.getName(), nameArgTypeMap, arg.getArrayDimensions(), funcUUID, argIndex));
        }
        return funcArgs;
    }

    /***
     * Helper function to format the return object as a JSON.
     * @param object - Return object
     * @param funcUUID - UUID of function
     * @param argSetIndex - Arg index. Used for accessing the write file in case the return type was a file.
     * @return - Json of formatted object
     */
    @SuppressWarnings("unchecked")
    public JsonElement formatReturnValueAsJSON(Object object, int funcUUID, int argSetIndex) {
        if (object == null)
            return null;
        Class objClass = object.getClass();
        if (objClass.isArray()) {
            JsonArray array = new JsonArray();
            for (Object obj: ReflectionHelper.toObjectArray(object)) {
                array.add(formatReturnValueAsJSON(obj, funcUUID, argSetIndex));
            }
            return array;
        } else if (FileHandler.isOutputClass(objClass.getCanonicalName())) {
            String fileContent = FileHandler.convertFileOutput(object, funcUUID, argSetIndex);
            if (fileContent != null)
                return new JsonPrimitive(fileContent);
            return null;
        } else if (Primitive.isValidType(object.getClass().getSimpleName())) {
            Primitive primitive = Primitive.getPrimitive(object.getClass().getSimpleName());
            return Primitive.convertToArgumentJSON(primitive, object.toString());
        }  else if (ObjectTypeArguments.isValidSystemClass(ReflectionHelper.makeKey(objClass))) {
            JsonObject jsonObject = new JsonObject();
            JsonObject returnObjectType = ObjectTypeArguments.getValidClassAsJson(objClass);
            // TODO: This method has to ideally be static
            for (JsonElement accessor: returnObjectType.getAsJsonArray("accessors")) {
                String methodName = accessor.getAsJsonObject().get("name").getAsString();
                try {
                    Method method = objClass.getDeclaredMethod(methodName);
                    method.setAccessible(true);
                    Object invocationResult = method.invoke(object);
                    jsonObject.add(methodName, formatReturnValueAsJSON(invocationResult, funcUUID, argSetIndex));
                } catch (NoSuchMethodException | IllegalAccessException | InvocationTargetException e) {
                    throw new RuntimeException(e);
                }
            }
            // TODO: Change this to support
            try {
                Map<String, Field> fields = ReflectionHelper.getFields(objClass);
                for (JsonElement variable: returnObjectType.getAsJsonArray("variables")) {
                    Field field = fields.get(variable.getAsJsonObject().get("name").getAsString());
                    field.setAccessible(true);
                    Object value = field.get(object);
                    if (field.getType().isArray()) {
                        JsonArray array = new JsonArray();
                        for (Object arrayElement: ReflectionHelper.toObjectArray(value)) {
                            array.add(formatReturnValueAsJSON(arrayElement, funcUUID, argSetIndex));
                        }
                        jsonObject.add(field.getName(), array);
                    } else {
                        String type = value.getClass().getSimpleName();
                        if (Primitive.isValidType(type)) {
                            Primitive primitive = Primitive.getPrimitive(type);
                            jsonObject.add(field.getName(), Primitive.convertToArgumentJSON(primitive, value.toString()));
                        } else {
                            jsonObject.add(field.getName(), formatReturnValueAsJSON(value, funcUUID, argSetIndex));
                        }
                    }
                }
            } catch (IllegalAccessException e) {
                throw new RuntimeException(e);
            }
            return jsonObject;
        } else {
            throw new RuntimeException(String.format("Failed to dump object of class: %s", objClass.getName()));
        }
    }

    public JsonObject getReturnMetadata() {
        if (this.returnVariable != null)
            return this.returnVariable.getMetadataAsJson();
        return null;
    }

    /**
     * Return method's return FunctionVariable's type as a string
     * @param method - Instance of java Reflection Method
     * @return - Method's return type as a string
     */
    public static String getMethodReturnTypeAsString(Method method) {
        Class returnType = method.getReturnType();
        StringBuilder arrDimensions = new StringBuilder();
        while (returnType.isArray()) {
            arrDimensions.append("[]");
            returnType = returnType.getComponentType();
        }
        String baseType = returnType.getSimpleName();
        if (returnType.getPackage() != null) {
            baseType = returnType.getCanonicalName().substring(returnType.getPackage().getName().length() + 1);
        }
        return String.format("%s%s", baseType, arrDimensions.toString());
    }

    /***
     * Encode the permutations of argument names by replacing "." with "$". This is because, mongo does not permit "." in dictionary keys
     * @param javaObj - Map of argument type and argument names.
     * @return - Encoded JSONObject
     */
    public static JsonObject encodeArgsPermutation(Map<String, List<String>> javaObj) {
        JsonObject json = new JsonObject();
        for (String key: javaObj.keySet()) {
            key = key.replace(".", "$");
            JsonArray array = new JsonArray();
            for (String value: javaObj.get(key)) {
                array.add(value);
            }
            json.add(key, array);
        }
        return json;
    }

    /***
     * Decode the permutations of argument names by replacing "$" with ".". This is because, mongo does not permit "." in dictionary keys
     * @param jsonObject - JSONObject of argument tupe and argument names
     * @return - Decoded map
     */
    public static Map<String, List<String>> decodeArgsPermutation(JsonObject jsonObject) {
        Map<String, List<String>> javaObj = new HashMap<>();
        for (String key: jsonObject.keySet()) {
            List<String> values = new ArrayList<>();
            for (JsonElement value: jsonObject.get(key).getAsJsonArray()) {
                values.add(value.getAsString());
            }
            key = key.replace("$", ".");
            javaObj.put(key, values);
        }
        return javaObj;
    }

    @Override
    public String toString() {
        return this.ast.toString();
    }

}

