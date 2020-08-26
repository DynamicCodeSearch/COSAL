package edu.ncsu.mos.blocks;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.reflect.TypeToken;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.blocks.ImportBlock;

import java.util.*;

public class CodeBlock {

    private final static Gson GSON = new Gson();

    private String uid;

    private String language;

    private String sourceFile;

    private String code;

    private String comments;

    private List<ImportBlock> imports;

    private boolean isStatic;

    private boolean isMethod;

    private boolean isClass;

    private boolean isFile;

    private String parentClassName;

    private String fileClassName;

    private String packageName;

    private String projectSourcePath;

    private String projectLangFolder;

    private Set<String> contextualTokens;

    private JsonObject ast;

    private ContestMeta contestMeta;

    public CodeBlock() {
        this.uid = Utils.randomString();
    }


    /***
     * Setters
     */

    public void setLanguage(String language) {
        this.language = language;
    }

    public void setSourceFile(String sourceFile) {
        this.sourceFile = sourceFile;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }

    public void setStatic(boolean aStatic) {
        isStatic = aStatic;
    }

    public void setProjectSourcePath(String projectSourcePath) {
        this.projectSourcePath = projectSourcePath;
    }

    public void setProjectLangFolder(String projectLangFolder) {
        this.projectLangFolder = projectLangFolder;
    }

    public void setImports(List<ImportBlock> imports) {
        this.imports = imports;
    }

    public void setMethod(boolean method) {
        isMethod = method;
    }

    public void setClass(boolean aClass) {
        isClass = aClass;
    }

    public void setFile(boolean file) {
        isFile = file;
    }

    public void setParentClassName(String parentClassName) {
        this.parentClassName = parentClassName;
    }

    public void setFileClassName(String fileClassName) {
        this.fileClassName = fileClassName;
    }

    public void setPackageName(String packageName) {
        this.packageName = packageName;
    }

    public void setContextualTokens(Set<String> contextualTokens) {
        this.contextualTokens = contextualTokens;
    }

    public void setAst(JsonObject ast) {
        this.ast = ast;
    }

    public void setAst(String ast) {
        this.ast = GSON.fromJson(ast, JsonObject.class);
    }

    public void setContestMeta(ContestMeta contestMeta) {
        this.contestMeta = contestMeta;
    }

    /***
     * Getters
     */

    public String getUid() {
        return uid;
    }

    public String getLanguage() {
        return language;
    }

    public String getSourceFile() {
        return sourceFile;
    }

    public String getCode() {
        return code;
    }

    public String getComments() {
        return comments;
    }

    public List<ImportBlock> getImports() {
        return imports;
    }

    public boolean isStatic() {
        return isStatic;
    }

    public boolean isMethod() {
        return isMethod;
    }

    public boolean isClass() {
        return isClass;
    }

    public boolean isFile() {
        return isFile;
    }

    public String getParentClassName() {
        return parentClassName;
    }

    public String getFileClassName() {
        return fileClassName;
    }

    public String getPackageName() {
        return packageName;
    }

    public String getProjectSourcePath() {
        return projectSourcePath;
    }

    public String getProjectLangFolder() {
        return projectLangFolder;
    }

    public Set<String> getContextualTokens() {
        return contextualTokens;
    }

    public JsonObject getAst() {
        return ast;
    }

    public ContestMeta getContestMeta() {
        return contestMeta;
    }

    public JsonObject toJson() {
        JsonObject json = new JsonObject();
        json.addProperty("uid", uid);
        json.addProperty("language", language);
        json.addProperty("sourceFile", Utils.getRepoLocalPath(sourceFile));
        json.addProperty("code", code);
        if (this.comments != null)
            json.addProperty("comments", comments);
        if (this.imports != null) {
            JsonArray importsJson = new JsonArray();
            for (ImportBlock importBlock: imports)
                importsJson.add(importBlock.toJson());
            json.add("imports", importsJson);
        }
        json.addProperty("isStatic", isStatic);
        json.addProperty("isMethod", isMethod);
        json.addProperty("isClass", isClass);
        json.addProperty("isFile", isFile);
        if (this.parentClassName != null)
            json.addProperty("parentClassName", parentClassName);
        if (this.fileClassName != null)
            json.addProperty("fileClassName", fileClassName);
        if (this.packageName != null)
            json.addProperty("packageName", packageName);
        if (this.projectSourcePath != null)
            json.addProperty("projectSourcePath", Utils.getRepoLocalPath(projectSourcePath));
        if (this.projectLangFolder != null)
            json.addProperty("projectLangFolder", Utils.getRepoLocalPath(projectLangFolder));
        if (this.contextualTokens != null)
            json.add("contextualTokens", new Gson().toJsonTree(this.contextualTokens).getAsJsonArray());
        if (this.ast != null)
            json.addProperty("ast", new Gson().toJson(this.ast));
        if (this.contestMeta != null)
            json.add("contestMeta", this.contestMeta.toJson());
        return json;
    }

    public static CodeBlock fromJson(JsonObject json) {
        CodeBlock codeBlock = new CodeBlock();
        codeBlock.uid = json.get("uid").getAsString();
        codeBlock.language = json.get("language").getAsString();
        codeBlock.sourceFile = Utils.getAbsolutePath(json.get("sourceFile").getAsString());
        codeBlock.code = json.get("code").getAsString();
        if (json.has("comments"))
            codeBlock.comments = json.get("comments").getAsString();
        if (json.has("imports")) {
            JsonArray importsJson = json.getAsJsonArray("imports");
            codeBlock.imports = new ArrayList<>();
            for (JsonElement importJson: importsJson)
                codeBlock.imports.add(ImportBlock.fromJson(importJson.getAsJsonObject()));
        }
        codeBlock.isStatic = json.get("isStatic").getAsBoolean();
        codeBlock.isMethod = json.get("isMethod").getAsBoolean();
        codeBlock.isClass = json.get("isClass").getAsBoolean();
        codeBlock.isFile = json.get("isFile").getAsBoolean();
        if (json.has("parentClassName"))
            codeBlock.parentClassName = json.get("parentClassName").getAsString();
        if (json.has("fileClassName"))
            codeBlock.fileClassName = json.get("fileClassName").getAsString();
        if (json.has("packageName"))
            codeBlock.packageName = json.get("packageName").getAsString();
        if (json.has("projectSourcePath"))
            codeBlock.projectSourcePath = Utils.getAbsolutePath(json.get("projectSourcePath").getAsString());
        if (json.has("projectLangFolder"))
            codeBlock.projectLangFolder = Utils.getAbsolutePath(json.get("projectLangFolder").getAsString());
        if (json.has("contextualTokens"))
            codeBlock.contextualTokens = GSON.fromJson(json.getAsJsonArray("contextualTokens"), new TypeToken<HashSet<String>>(){}.getType());
        if (json.has("ast"))
            codeBlock.ast = GSON.fromJson(json.get("ast").getAsString(), JsonObject.class);
        if (json.has("contestMeta"))
            codeBlock.setContestMeta(ContestMeta.fromJson(json.getAsJsonObject("contestMeta")));
        return codeBlock;
    }
}
