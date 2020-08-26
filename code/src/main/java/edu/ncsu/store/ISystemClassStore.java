package edu.ncsu.store;

import com.google.gson.JsonObject;

public interface ISystemClassStore {

    public void saveClass(JsonObject classData);

    public JsonObject loadClass(String projectName, String classKey);

    public JsonObject loadConstructorJSON(String classKey, String constructorKey);

    public boolean isSystemClassValiditySaved(String projectName, String classKey);

    public boolean isValidSystemClass(String projectName, String classKey);

    public void updateSystemClassValidity(String projectName, String classKey, boolean isValid);

}
