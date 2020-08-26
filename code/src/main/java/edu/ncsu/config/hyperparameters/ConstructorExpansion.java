package edu.ncsu.config.hyperparameters;

public enum ConstructorExpansion {

    OPTIMAL(1, "Optimal"),
    ALL(2, "All");

    private int id;

    private String type;

    private ConstructorExpansion(int id, String type) {
        this.id = id;
        this.type = type;
    }

    public int getId() {
        return id;
    }

    public String getType() {
        return type;
    }

    @Override
    public String toString() {
        return String.format("Constructor Expansion: %d-%s", this.getId(), this.getType());
    }
}
