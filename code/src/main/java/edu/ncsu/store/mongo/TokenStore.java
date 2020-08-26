package edu.ncsu.store.mongo;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonPrimitive;
import com.google.gson.reflect.TypeToken;
import com.mongodb.QueryBuilder;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.store.ITokenStore;
import org.bson.BSONObject;
import org.bson.Document;
import org.bson.conversions.Bson;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class TokenStore implements ITokenStore {

    private static final String TOKENS_COLLECTION = "functions_tokens";

    private static final String CONTEXT_COLLECTION = "functions_contexts";

    @Override
    public void saveTokens(JsonObject tokenJson) {
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, TOKENS_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "hash_key");
        Bson query = Filters.eq("hash_key", tokenJson.get("hash_key").getAsLong());
        Document existingDoc = MongoDriver.getDocument(collection, query);
        String functionName = tokenJson.get("name").getAsString();
        Document document = MongoDriver.parseAsDocument(tokenJson);
        if (existingDoc != null) {
            JsonArray names = MongoDriver.parseAsJson(existingDoc).getAsJsonArray("names");
            Set<String> namesSet = new Gson().fromJson(names, new TypeToken<HashSet<String>>(){}.getType());
            if (!namesSet.contains(functionName)) {
                namesSet.add(functionName);
                Document namesDoc = new Document("$set", new Document("names", new ArrayList<>(namesSet)));
                MongoDriver.updateDocument(collection, query, namesDoc);
            }
        } else {
            JsonArray names = new JsonArray();
            names.add(functionName);
            tokenJson.add("names", names);
            tokenJson.remove("name");
            collection.insertOne(MongoDriver.parseAsDocument(tokenJson));
        }
    }

    @Override
    public void saveContextualTokens(JsonObject contextJson) {
        MongoCollection<Document> collection = MongoDriver.getCollection(ProjectConfig.DATASET, CONTEXT_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "hash_key");
        Bson query = Filters.eq("hash_key", contextJson.get("hash_key").getAsLong());
        Document existingDoc = MongoDriver.getDocument(collection, query);
        String functionName = contextJson.get("name").getAsString();
        if (existingDoc != null) {
            JsonArray names = MongoDriver.parseAsJson(existingDoc).getAsJsonArray("names");
            Set<String> namesSet = new Gson().fromJson(names, new TypeToken<HashSet<String>>(){}.getType());
            if (!namesSet.contains(functionName)) {
                namesSet.add(functionName);
                Document namesDoc = new Document("$set", new Document("names", new ArrayList<>(namesSet)));
                MongoDriver.updateDocument(collection, query, namesDoc);
            }
        } else {
            JsonArray names = new JsonArray();
            names.add(functionName);
            contextJson.add("names", names);
            contextJson.remove("name");
            collection.insertOne(MongoDriver.parseAsDocument(contextJson));
        }
    }
}
