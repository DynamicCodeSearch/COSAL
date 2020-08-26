package edu.ncsu.mos.store;

import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.UpdateOptions;
import com.mongodb.client.model.Updates;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.store.mongo.MongoDriver;
import edu.ncsu.utils.Utils;
import org.bson.Document;
import org.bson.conversions.Bson;

import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.logging.Logger;

public class MetaStore {

    private static final Logger LOGGER = Logger.getLogger(MetaStore.class.getName());

    private static final String META_STORE_COLLECTION = "meta_store";

    private static final String JAVA_FILES_EXECUTED = "java_files_executed";

    public void updateFileProcessed(String filePath) {
        filePath = Utils.getRepoLocalPath(filePath);
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, META_STORE_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "key");
        Bson query = Filters.eq("key", JAVA_FILES_EXECUTED);
        UpdateOptions options = new UpdateOptions().upsert(true);
        collection.updateOne(query, Updates.addToSet("value", filePath),  options);
    }

    public boolean isFileProcessed(String filePath) {
        filePath = Utils.getRepoLocalPath(filePath);
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, META_STORE_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            return false;
        Bson query = Filters.eq("key", JAVA_FILES_EXECUTED);
        Document document = MongoDriver.getDocument(collection, query);
        if (document == null)
            return false;
        Set<String> files = new HashSet<>((List<String>) document.get("value"));
        return files.contains(filePath);
    }

}
