package edu.ncsu.store.mongo;

import com.google.gson.JsonObject;
import com.mongodb.client.MongoCollection;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.store.ICommonStore;
import org.bson.Document;

import java.util.logging.Logger;

public class CommonStore implements ICommonStore {

    private static final Logger LOGGER = Logger.getLogger(CommonStore.class.getName());

    private static final String TEST_COLLECTION = "test_collection";

    @Override
    public void initializeDataset() {
        String dataset = ProjectConfig.DATASET;
        LOGGER.info(String.format("Initializing database: '%s': ", dataset));
        MongoCollection<Document> collection = MongoDriver.getCollection(dataset, TEST_COLLECTION);
        if (!MongoDriver.collectionExists(collection) || collection.count() == 0) {
            JsonObject document = new JsonObject();
            document.addProperty("name", "Hello World!");
            collection.insertOne(MongoDriver.parseAsDocument(document));
        }
    }

    @Override
    public void clearStoreForProject() {
        String dataset = ProjectConfig.DATASET;
        String project = ProjectConfig.PROJECT_NAME;
        MongoCollection<Document> collection;

        LOGGER.info(String.format("Deleting snipped functions for project: '%s'", project));
        collection = MongoDriver.getCollection(dataset, MetadataStore.FUNCTION_METADATA_COLLECTION);
        if (MongoDriver.collectionExists(collection))
            MongoDriver.deleteDocument(collection, "project", project);

        LOGGER.info(String.format("Deleting executed functions for project: '%s'", project));
        FunctionStore functionStore = new FunctionStore(dataset);
        collection = MongoDriver.getCollection(dataset, functionStore.getSuccessFunctionsCollection());
        if (MongoDriver.collectionExists(collection))
            MongoDriver.deleteDocument(collection, "project", project);

        LOGGER.info(String.format("Deleting failed functions for project: '%s'", project));
        collection = MongoDriver.getCollection(dataset, functionStore.getFailedFunctionsCollection());
        if (MongoDriver.collectionExists(collection))
            MongoDriver.deleteDocument(collection, "project", project);

        LOGGER.info(String.format("Deleting system classes for project: '%s'", project));
        collection = MongoDriver.getCollection(dataset, SystemClassStore.SYSTEM_CLASS_COLLECTION);
        if (MongoDriver.collectionExists(collection))
            MongoDriver.deleteDocument(collection, "project", project);
        collection = MongoDriver.getCollection(dataset, SystemClassStore.SYSTEM_CLASS_VALIDITY_COLLECTION);
        if (MongoDriver.collectionExists(collection))
            MongoDriver.deleteDocument(collection, "project", project);
    }

    @Override
    public void clearStoreForDataset() {
        MongoDriver.dropDatabase(ProjectConfig.DATASET);
    }
}
