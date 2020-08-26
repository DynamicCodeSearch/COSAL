package edu.ncsu.store.json;

import com.google.gson.JsonObject;
import edu.ncsu.store.IMetadataStore;

import java.util.List;
import java.util.Map;

public class MetadataStore implements IMetadataStore {

    private String dataset;

    public MetadataStore(String dataset) {
        this.dataset = dataset;
    }

    @Override
    public void saveClassFunctionMetadata(JsonObject generatedFunction) {
        throw new RuntimeException("This method is not implemented for JSON. Check out Mongo.");
    }

    @Override
    public void saveClassFunctionsMetadata(List<JsonObject> generatedFunctions) {
        throw new RuntimeException("This method is not implemented for JSON. Check out Mongo.");
    }

    @Override
    public JsonObject getFunctionMetadata(String functionName) {
        throw new RuntimeException("This method is not implemented for JSON. Check out Mongo.");
    }

    @Override
    public Map<String, JsonObject> getFunctionsMetadata(Map<String, Object> query) {
        throw new RuntimeException("This method is not implemented for JSON. Check out Mongo.");
    }

    @Override
    public String getSourceFile(String functionName) {
        throw new RuntimeException("This method is not implemented for JSON. Check out Mongo.");
    }

    @Override
    public void deleteClassFunctionMetadata(String functionName) {
        throw new RuntimeException("This method is not implemented for JSON. Check out Mongo.");
    }

    @Override
    public void deleteClassFunctionsMetadata(String filePath) {
        throw new RuntimeException("This method is not implemented for JSON. Check out Mongo.");
    }

    @Override
    public void deleteClassFunctionsMetadata(List<String> functionNames) {
        throw new RuntimeException("This method is not implemented for JSON. Check out Mongo.");
    }

    @Override
    public void updateFunctionMetadata(String functionName, String attribute, Object value) {
        throw new RuntimeException("This method is not implemented for JSON. Check out Mongo.");
    }

    @Override
    public Map<String, JsonObject> loadGeneratedFunctionBodies() {
        throw new RuntimeException("This method is not implemented for JSON. Check out Mongo.");
    }
}
