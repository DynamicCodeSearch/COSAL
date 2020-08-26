package edu.ncsu.store;

import com.google.gson.JsonObject;

import java.util.List;
import java.util.Map;

public interface IMetadataStore {

    public void saveClassFunctionMetadata(JsonObject generatedFunction);

    public void saveClassFunctionsMetadata(List<JsonObject> generatedFunctions);

    public JsonObject getFunctionMetadata(String functionName);

    public Map<String, JsonObject> getFunctionsMetadata(Map<String, Object> query);

    public String getSourceFile(String functionName);

    public void deleteClassFunctionMetadata(String functionName);

    public void deleteClassFunctionsMetadata(String filePath);

    public void deleteClassFunctionsMetadata(List<String> functionNames);

    public void updateFunctionMetadata(String functionName, String attribute, Object value);

    public Map<String, JsonObject> loadGeneratedFunctionBodies();

}
