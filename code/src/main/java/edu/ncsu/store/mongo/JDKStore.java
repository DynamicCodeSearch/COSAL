package edu.ncsu.store.mongo;

import com.google.gson.JsonObject;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.store.IJDKStore;
import org.bson.Document;
import org.bson.conversions.Bson;

import java.util.logging.Logger;

public class JDKStore implements IJDKStore {
    private static final Logger LOGGER = Logger.getLogger(JDKStore.class.getName());

    private static final String JDK_METHODS_COLLECTION = "jdk_methods";

    protected String dataset;

    public JDKStore(String dataset) {
        this.dataset = dataset;
    }

    public JDKStore() {
        this(ProjectConfig.DATASET);
    }

    @Override
    public void saveMethod(JsonObject methodData) {
        String methodKey = methodData.get("key").getAsString();
        LOGGER.info(String.format("Saving method '%s' to DB ...", methodKey));
        MongoCollection<Document> collection = MongoDriver.getCollection(dataset, JDK_METHODS_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "key");
        Bson filter = Filters.eq("key", methodKey);
        if (!MongoDriver.containsDocument(collection, filter)) {
            collection.insertOne(MongoDriver.parseAsDocument(methodData));
            LOGGER.info(String.format("Saved method '%s' to DB!", methodKey));
        }
    }

    @Override
    public JsonObject loadMethod(String key) {
        Bson filter = Filters.eq("key", key);
        MongoCollection<Document> collection = MongoDriver.getCollection(dataset, JDK_METHODS_COLLECTION);
        Document document = MongoDriver.getDocument(collection, filter);
        if (document != null)
            return MongoDriver.parseAsJson(document);
        return null;
    }
}
