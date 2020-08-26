package edu.ncsu.store;

import com.google.gson.JsonObject;

public interface ITokenStore {

    public void saveTokens(JsonObject tokenJson);

    public void saveContextualTokens(JsonObject contextJson);

}
