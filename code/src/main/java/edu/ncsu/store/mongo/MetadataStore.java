package edu.ncsu.store.mongo;

import com.google.gson.JsonObject;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.utils.Utils;
import org.bson.Document;
import org.bson.conversions.Bson;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Logger;

public class MetadataStore implements IMetadataStore {

    private static final Logger LOGGER = Logger.getLogger(MetadataStore.class.getName());

    protected static final String FUNCTION_METADATA_COLLECTION = "functions_metadata";

    private String dataset;

    public MetadataStore(String dataset) {
        this.dataset = dataset;
    }

    @Override
    public void saveClassFunctionMetadata(JsonObject generatedFunction) {
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, FUNCTION_METADATA_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "name");
        String functionName = generatedFunction.get("name").getAsString();
        Document document = MongoDriver.parseAsDocument(generatedFunction);
        if (MongoDriver.containsDocument(collection, "name", functionName))
            MongoDriver.deleteDocument(collection, "name", functionName);
        collection.insertOne(document);
    }

    @Override
    public void saveClassFunctionsMetadata(List<JsonObject> generatedFunctions) {
        LOGGER.info("Writing metadata in Mongo Database ... ");
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, FUNCTION_METADATA_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "name");
        for (JsonObject generatedFunction: generatedFunctions) {
            String functionName = generatedFunction.get("name").getAsString();
            Document document = MongoDriver.parseAsDocument(generatedFunction);
            if (MongoDriver.containsDocument(collection, "name", functionName))
                MongoDriver.deleteDocument(collection, "name", functionName);
            collection.insertOne(document);
        }
    }

    @Override
    @SuppressWarnings("rawtypes")
    public Map<String, JsonObject> getFunctionsMetadata(Map<String, Object> query) {
        Document queryBson = new Document();
        query.forEach(queryBson::append);
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, FUNCTION_METADATA_COLLECTION);
        FindIterable iterator = MongoDriver.getDocuments(collection, queryBson);
        Map<String, JsonObject> functionsMetadata = new HashMap<>();
        if (iterator == null)
            return functionsMetadata;
        for (Object doc: iterator) {
            JsonObject functionJson = MongoDriver.parseAsJson((Document) doc);
            functionsMetadata.put(functionJson.get("name").getAsString(), functionJson);
        }
        return functionsMetadata;
    }

    @Override
    public JsonObject getFunctionMetadata(String functionName) {
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, FUNCTION_METADATA_COLLECTION);
        Document document = MongoDriver.getDocument(collection, "name", functionName);
        if (document == null) {
            return null;
//            throw new RuntimeException(String.format("Document is null for function '%s'", functionName));
        }
        return MongoDriver.parseAsJson(document);
    }

    @Override
    public String getSourceFile(String functionName) {
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, FUNCTION_METADATA_COLLECTION);
        Document document = MongoDriver.getDocument(collection, "name", functionName);
        if (document == null)
            return null;
        return Utils.getAbsolutePath(document.get("filePath").toString());
    }

    @Override
    public void deleteClassFunctionMetadata(String functionName) {
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, FUNCTION_METADATA_COLLECTION);
        MongoDriver.deleteDocument(collection, Filters.eq("name", functionName));
    }

    @Override
    public void deleteClassFunctionsMetadata(String filePath) {
        LOGGER.info(String.format("Deleting function metadata for filePath : '%s' ... ", filePath));
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, FUNCTION_METADATA_COLLECTION);
        MongoDriver.deleteDocument(collection, Filters.eq("filePath", filePath));
    }

    @Override
    public void deleteClassFunctionsMetadata(List<String> functionNames) {
        LOGGER.info(String.format("Deleting function metadata for '%d' functions ... ", functionNames.size()));
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, FUNCTION_METADATA_COLLECTION);
        for (String functionName : functionNames) {
            MongoDriver.deleteDocument(collection, Filters.eq("name", functionName ));
        }
    }

    public void updateFunctionMetadata(String functionName, String attribute, Object value) {
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, FUNCTION_METADATA_COLLECTION);
        Bson query = Filters.eq("name", functionName);
        Bson update = new Document("$set", new Document(attribute, value));
        MongoDriver.updateDocument(collection, query, update);
    }

    @Override
    @SuppressWarnings("rawtypes")
    public Map<String, JsonObject> loadGeneratedFunctionBodies() {
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, FUNCTION_METADATA_COLLECTION);
//        Bson query = Filters.eq("originalFunctionName", Filters.exists("originalFunctionName", false));
        Bson query = Filters.exists("originalFunctionName", false);
        FindIterable iterator = MongoDriver.getDocuments(collection, query);
        Map<String, JsonObject> functionsMetadata = new HashMap<>();
        if (iterator == null)
            return functionsMetadata;
        for (Object doc: iterator) {
            JsonObject functionJson = MongoDriver.parseAsJson((Document) doc);
            functionsMetadata.put(functionJson.get("name").getAsString(), functionJson);
        }
        return functionsMetadata;
    }
}
