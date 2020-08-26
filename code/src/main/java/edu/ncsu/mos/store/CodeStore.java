package edu.ncsu.mos.store;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.Projections;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.mos.blocks.CodeBlock;
import edu.ncsu.store.mongo.MongoDriver;
import edu.ncsu.utils.Utils;
import org.bson.Document;
import org.bson.conversions.Bson;

import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

public class CodeStore {

    private static final Logger LOGGER = Logger.getLogger(CodeStore.class.getName());

    private static final String CODE_STORE_COLLECTION = "code_store";

    private static final String FILE_STORE_COLLECTION = "file_store";

    public void saveCodeBlock(CodeBlock codeBlock) {
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, CODE_STORE_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "uid");
        Document document = MongoDriver.parseAsDocument(codeBlock.toJson());
        String uid = document.getString("uid");
        if (MongoDriver.containsDocument(collection, "uid", uid))
            MongoDriver.deleteDocument(collection, "uid", uid);
        collection.insertOne(document);
    }

    public void deleteCodeBlockFromFile(String filePath) {
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, CODE_STORE_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            return;
        filePath = Utils.getRepoLocalPath(filePath);
        Bson query = Filters.eq("sourceFile", filePath);
        MongoDriver.deleteDocument(collection, query);
    }

    public List<CodeBlock> getCodeBlocksForFile(String filePath, boolean onlyStatic, boolean onlyBody) {
        List<CodeBlock> codeBlocks = new ArrayList<>();
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, CODE_STORE_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            return codeBlocks;
        filePath = Utils.getRepoLocalPath(filePath);
        Bson query = Filters.eq("sourceFile", filePath);
        if (onlyStatic)
            query = Filters.and(query, Filters.eq("isStatic", true));
        FindIterable documents;
        if (onlyBody) {
            documents = MongoDriver.getDocuments(collection, query, Projections.exclude("ast", "contextualTokens"));
        } else {
            documents = MongoDriver.getDocuments(collection, query);
        }
        long n_documents = MongoDriver.countDocuments(collection, query);
        if (n_documents <= 1)
            return null;
        if (documents == null)
            return codeBlocks;
        for (Object doc: documents) {
            JsonObject codeBlockJson = MongoDriver.parseAsJson((Document) doc);
            codeBlocks.add(CodeBlock.fromJson(codeBlockJson));
        }
        return codeBlocks;
    }

    public void saveFileBlock(CodeBlock codeBlock) {
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, FILE_STORE_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "uid", "sourceFile");
        Document document = MongoDriver.parseAsDocument(codeBlock.toJson());
        String sourceFile = document.getString("sourceFile");
        if (MongoDriver.containsDocument(collection, "sourceFile", sourceFile))
            MongoDriver.deleteDocument(collection, "sourceFile", sourceFile);
        collection.insertOne(document);
    }

    public CodeBlock getFileBlock(String sourceFilePath) {
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, FILE_STORE_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            return null;
        Bson query = Filters.eq("sourceFile", Utils.getRepoLocalPath(sourceFilePath));
        Document document = MongoDriver.getDocument(collection, query);
        if (document == null)
            return null;
        return CodeBlock.fromJson(MongoDriver.parseAsJson(document));
    }

    public void deleteAllFileBlocks() {
        LOGGER.info("Deleting all file blocks ... ");
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, FILE_STORE_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            return;
        Bson query = Filters.eq("language", Settings.LANGUAGE_JAVA);
        collection.deleteMany(query);
    }

}
