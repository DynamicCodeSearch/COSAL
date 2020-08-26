package edu.ncsu.visitors.blocks;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.utils.Utils;

import java.util.Set;

public class GeneratedFunction {

    private String project;

    private String name;

    private String originalFunctionName;

    private String sourceCodeFunctionName;

    private String sourceCodeClassName;

    private String body;

    private String inputKey;

    private String sourceFile;

    private String generatedFile;

    private Set<Integer> linesTouched;

    private Set<Integer> span;

    private JsonObject returnMeta;

    private boolean isWholeMethod = false;

    private String functionDescriptorString;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getOriginalFunctionName() {
        return originalFunctionName;
    }

    public void setOriginalFunctionName(String originalFunctionName) {
        this.originalFunctionName = originalFunctionName;
    }

    public String getSourceCodeFunctionName() {
        return sourceCodeFunctionName;
    }

    public void setSourceCodeFunctionName(String sourceCodeFunctionName) {
        this.sourceCodeFunctionName = sourceCodeFunctionName;
    }

    public String getSourceCodeClassName() {
        return sourceCodeClassName;
    }

    public void setSourceCodeClassName(String sourceCodeClassName) {
        this.sourceCodeClassName = sourceCodeClassName;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public String getInputKey() {
        return inputKey;
    }

    public void setInputKey(String inputKey) {
        this.inputKey = inputKey;
    }

    public String getSourceFile() {
        return sourceFile;
    }

    public void setSourceFile(String sourceFile) {
        this.sourceFile = sourceFile;
    }

    public String getGeneratedFile() {
        return generatedFile;
    }

    public void setGeneratedFile(String generatedFile) {
        this.generatedFile = generatedFile;
    }

    public Set<Integer> getLinesTouched() {
        return linesTouched;
    }

    public void setLinesTouched(Set<Integer> linesTouched) {
        this.linesTouched = linesTouched;
    }

    public Set<Integer> getSpan() {
        return span;
    }

    public void setSpan(Set<Integer> span) {
        this.span = span;
    }

    public JsonObject getReturnMeta() {
        return returnMeta;
    }

    public void setReturnMeta(JsonObject returnMeta) {
        this.returnMeta = returnMeta;
    }

    public boolean isWholeMethod() {
        return isWholeMethod;
    }

    public void setWholeMethod(boolean wholeMethod) {
        isWholeMethod = wholeMethod;
    }

    public void setFunctionDescriptorString(String functionDescriptorString) {
        this.functionDescriptorString = functionDescriptorString;
    }

    public String getFunctionDescriptorString() {
        return functionDescriptorString;
    }

    public GeneratedFunction() {
        this.project = ProjectConfig.PROJECT_NAME;
    }

    public JsonObject toJson() {
        JsonObject json = new JsonObject();
        json.addProperty("name", name);
        json.addProperty("originalFunctionName", originalFunctionName);
        json.addProperty("sourceCodeFunctionName", sourceCodeFunctionName);
        json.addProperty("sourceCodeClassName", sourceCodeClassName);
        json.addProperty("project", project);
        json.addProperty("body", body);
        json.addProperty("inputKey", inputKey);
        json.addProperty("isWholeMethod", isWholeMethod);
        json.addProperty("filePath", Utils.getRepoLocalPath(generatedFile));
        json.addProperty("baseFilePath", Utils.getRepoLocalPath(sourceFile));
        if (this.linesTouched != null && this.linesTouched.size() > 0) {
            JsonArray linesTouched = new JsonArray();
            for (Integer line: this.linesTouched)
                linesTouched.add(line);
            json.add("linesTouched", linesTouched);
        }
        if (this.span != null) {
            JsonArray span = new JsonArray();
            for (Integer line: this.span)
                span.add(line);
            json.add("span", span);
        }
        if (this.returnMeta != null) {
            json.add("return", returnMeta);
        }
//        json.add("argNamesKeysMap", Utils.toJson(getArgComboKeyMap()));
        return json;
    }

}
