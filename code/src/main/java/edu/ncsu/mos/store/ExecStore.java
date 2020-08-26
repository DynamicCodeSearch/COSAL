package edu.ncsu.mos.store;


import com.google.gson.JsonObject;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.store.mongo.MongoDriver;
import edu.ncsu.utils.Utils;
import org.bson.Document;
import org.bson.conversions.Bson;

import java.util.logging.Logger;

public class ExecStore {

    private static final Logger LOGGER = Logger.getLogger(ExecStore.class.getName());

    private static final String FUNCTION_METADATA_COLLECTION = "functions_metadata";

    private static final String FUNCTIONS_EXECUTED_COLLECTION = "functions_executed";

    private static final String FUNCTIONS_FAILED_COLLECTION = "functions_failed";

    public void saveClassFunctionMetadata(JsonObject functionMeta) {
        String filePath = Utils.getRepoLocalPath(functionMeta.get("filePath").getAsString());
        functionMeta.addProperty("filePath", filePath);
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, FUNCTION_METADATA_COLLECTION);
        if (!MongoDriver.collectionExists(collection)) {
            MongoDriver.createNonUniqueIndexForCollection(collection, "originalFunctionName");
            MongoDriver.createNonUniqueIndexForCollection(collection, "filePath");
        }
        Document document = MongoDriver.parseAsDocument(functionMeta);
        collection.insertOne(document);
    }

    public void deleteClassFunctionMetadata(String filePath, String originalFunctionName) {
        filePath = Utils.getRepoLocalPath(filePath);
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, FUNCTION_METADATA_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            return;
        Bson query = Filters.and(Filters.eq("filePath", filePath), Filters.eq("originalFunctionName", originalFunctionName));
        if (MongoDriver.containsDocument(collection, query))
            MongoDriver.deleteDocument(collection, query);

    }

    private void updateFunction(JsonObject result, String collectionName) {
        String filePath = Utils.getRepoLocalPath(result.get("filePath").getAsString());
        result.addProperty("filePath", filePath);
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, collectionName);
        if (!MongoDriver.collectionExists(collection)) {
            MongoDriver.createNonUniqueIndexForCollection(collection, "originalFunctionName");
            MongoDriver.createNonUniqueIndexForCollection(collection, "filePath");
        }
        Document document = MongoDriver.parseAsDocument(result);
        collection.insertOne(document);
    }

    public void updateFunctionResult(JsonObject result) {
        updateFunction(result, FUNCTIONS_EXECUTED_COLLECTION);
    }

    public void updateFunctionError(JsonObject result) {
        updateFunction(result, FUNCTIONS_FAILED_COLLECTION);
    }

    public void deleteClassFunctionResult(String filePath, String originalFunctionName) {
        filePath = Utils.getRepoLocalPath(filePath);
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, FUNCTIONS_FAILED_COLLECTION);
        Bson query = Filters.and(Filters.eq("filePath", filePath), Filters.eq("originalFunctionName", originalFunctionName));
        if (MongoDriver.collectionExists(collection) && MongoDriver.containsDocument(collection, query))
            MongoDriver.deleteDocument(collection, query);
        collection = MongoDriver.getCollection(ProjectConfig.DATASET, FUNCTIONS_EXECUTED_COLLECTION);
        if (MongoDriver.collectionExists(collection) && MongoDriver.containsDocument(collection, query))
            MongoDriver.deleteDocument(collection, query);
    }

}
