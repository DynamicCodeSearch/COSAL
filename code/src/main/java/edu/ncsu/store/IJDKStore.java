package edu.ncsu.store;

import com.google.gson.JsonObject;

public interface IJDKStore {

    public void saveMethod(JsonObject methodData);

    public JsonObject loadMethod(String key);
}
