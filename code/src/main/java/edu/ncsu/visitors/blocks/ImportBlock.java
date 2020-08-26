package edu.ncsu.visitors.blocks;

import com.github.javaparser.ast.ImportDeclaration;
import com.google.gson.JsonObject;

public class ImportBlock {

    /**
     * `java.util` in `java.util.List`
     */
    private String qualifier;

    /***
     * Name of the import. eg. `List` in `java.util.List`
     */
    private String name;

    /***
     * If it is a static import
     */
    private boolean isStatic;

    /***
     * If it ends with asterisk
     */
    private boolean isAsterisk;

    public String getName() {
        return name;
    }

    public String getQualifier() {
        return qualifier;
    }

    public boolean isStatic() {
        return isStatic;
    }

    public boolean isAsterisk() {
        return isAsterisk;
    }

    private ImportBlock() {}

    public ImportBlock(ImportDeclaration importDeclaration) {
        this.name = importDeclaration.getName().getIdentifier();
        if (importDeclaration.getName().getQualifier().isPresent())
            this.qualifier = importDeclaration.getName().getQualifier().get().asString();
        this.isAsterisk = importDeclaration.isAsterisk();
        this.isStatic = importDeclaration.isStatic();
    }

    public JsonObject toJson() {
        JsonObject json = new JsonObject();
        json.addProperty("name", name);
        if (qualifier != null)
            json.addProperty("qualifier", qualifier);
        if (isStatic)
            json.addProperty("isStatic", isStatic);
        if (isAsterisk)
            json.addProperty("isAsterisk", isAsterisk);
        return json;
    }

    public static ImportBlock fromJson(JsonObject json) {
        ImportBlock importBlock = new ImportBlock();
        importBlock.name = json.get("name").getAsString();
        if (json.has("qualifier"))
            importBlock.qualifier = json.get("qualifier").getAsString();
        if (json.has("isStatic"))
            importBlock.isStatic = json.get("isStatic").getAsBoolean();
        if (json.has("isAsterisk"))
            importBlock.isAsterisk = json.get("isAsterisk").getAsBoolean();
        return importBlock;
    }

}
