package edu.ncsu.store.mongo;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;
import edu.ncsu.store.ISystemClassStore;
import org.bson.Document;
import org.bson.conversions.Bson;

import java.awt.*;
import java.util.logging.Logger;

public class SystemClassStore implements ISystemClassStore {

    private static final Logger LOGGER = Logger.getLogger(SystemClassStore.class.getName());

    protected static final String SYSTEM_CLASS_COLLECTION = "system_classes";

    protected static final String SYSTEM_CLASS_VALIDITY_COLLECTION = "system_classes_validity";

    protected String dataset;

    public SystemClassStore(String dataset) {
        this.dataset = dataset;
    }

    @Override
    public void saveClass(JsonObject classData) {
        String classKey = classData.get("key").getAsString();
        String projectName = classData.get("project").getAsString();
        LOGGER.info(String.format("Saving class '%s' to DB ...", classKey));
        MongoCollection<Document> collection = MongoDriver.getCollection(dataset, SYSTEM_CLASS_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "key", "project");
        Bson filter =
                Filters.and(Filters.eq("key", classKey),  Filters.eq("project", projectName));
        if (!MongoDriver.containsDocument(collection, filter)) {
            collection.insertOne(MongoDriver.parseAsDocument(classData));
            LOGGER.info(String.format("Saved class '%s' to DB!", classKey));
        }
    }

    @Override
    public JsonObject loadClass(String projectName, String classKey) {
        Bson filter =
                Filters.and(Filters.eq("key", classKey),  Filters.eq("project", projectName));
        MongoCollection<Document> collection = MongoDriver.getCollection(dataset, SYSTEM_CLASS_COLLECTION);
        Document document = MongoDriver.getDocument(collection, filter);
        if (document != null)
            return MongoDriver.parseAsJson(document);
        return null;
    }

    public JsonObject loadConstructorJSON(String classKey, String constructorKey) {
        MongoCollection<Document> collection = MongoDriver.getCollection(dataset, SYSTEM_CLASS_COLLECTION);
        Document classDocument = MongoDriver.getDocument(collection, "key", classKey);
        if (classDocument == null)
            return null;
        JsonObject classJsonObject = MongoDriver.parseAsJson(classDocument);
        for (JsonElement constructor: classJsonObject.get("constructors").getAsJsonArray()) {
            JsonObject constructorObj = constructor.getAsJsonObject();
            if (constructorObj.get("key").getAsString().equals(constructorKey))
                return constructorObj;
        }
        return null;
    }

    @Override
    public boolean isSystemClassValiditySaved(String projectName, String classKey) {
        MongoCollection<Document> collection = MongoDriver.getCollection(dataset, SYSTEM_CLASS_VALIDITY_COLLECTION);
        Bson filter =
                Filters.and(Filters.eq("key", classKey),  Filters.eq("project", projectName));
        return MongoDriver.collectionExists(collection) && MongoDriver.containsDocument(collection, filter);
    }

    @Override
    public boolean isValidSystemClass(String projectName, String classKey) {
        MongoCollection<Document> collection = MongoDriver.getCollection(dataset, SYSTEM_CLASS_VALIDITY_COLLECTION);
        Bson filter =
                Filters.and(Filters.eq("key", classKey),  Filters.eq("project", projectName));
        if (!MongoDriver.collectionExists(collection))
            return false;
        Document doc = MongoDriver.getDocument(collection, filter);
        return doc != null && (Boolean) doc.get("isValid");
    }

    @Override
    public void updateSystemClassValidity(String projectName, String classKey, boolean isValid) {
        MongoCollection<Document> collection = MongoDriver.getCollection(dataset, SYSTEM_CLASS_VALIDITY_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "key", "project");
        Bson filter =
                Filters.and(Filters.eq("key", classKey),  Filters.eq("project", projectName));
        JsonObject classValidityJson = new JsonObject();
        classValidityJson.addProperty("key", classKey);
        classValidityJson.addProperty("project", projectName);
        classValidityJson.addProperty("isValid", isValid);
        if (!MongoDriver.containsDocument(collection, filter)) {
            collection.insertOne(MongoDriver.parseAsDocument(classValidityJson));
            LOGGER.info(String.format("Saved validity of class '%s' to DB!", classKey));
        }
    }

}
