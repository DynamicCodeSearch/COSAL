package edu.ncsu.executors.models;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import java.util.List;

public class SystemClassConstructor {

    private JsonObject constructorJson;

    private List<FunctionVariable> arguments;

    public void setJsonObject(JsonObject constructorJson) {
        this.constructorJson = constructorJson;
    }

    public JsonObject getJsonObject() {
        return constructorJson;
    }

    public List<FunctionVariable> getArguments() {
        return arguments;
    }

    public SystemClassConstructor(JsonObject constructorJson, List<FunctionVariable> arguments) {
        this.constructorJson = constructorJson;
        this.arguments = arguments;
    }

    public JsonObject makeMetadata() {
        JsonObject metadata = new JsonObject();
        metadata.addProperty("classKey", constructorJson.get("classKey").getAsString());
        metadata.addProperty("key", constructorJson.get("key").getAsString());
        JsonArray argsJson = new JsonArray();
        for (FunctionVariable argument: arguments) {
            argsJson.add(argument.getMetadataAsJson());
        }
        metadata.add("argsMetadata", argsJson);
        return metadata;
    }

    public int getTotalArguments() {
        if (this.constructorJson == null)
            return 0;
        return constructorJson.get("totalParams").getAsInt();
    }

    public String getClassKey() {
        if (this.constructorJson != null && this.constructorJson.has("classKey"))
            return constructorJson.get("classKey").getAsString();
        return null;
    }
}
