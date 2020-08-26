package edu.ncsu.config.hyperparameters;

public enum SnipperMode {

    STATEMENT(1, "Statement"),
    METHOD(2, "Method");

    private int id;

    private String mode;

    private SnipperMode(int id, String mode) {
        this.id = id;
        this.mode = mode;
    }

    public int getId() {
        return id;
    }

    public String getMode() {
        return mode;
    }

    @Override
    public String toString() {
        return String.format("Snipper Mode: %d-%s", getId(), getMode());
    }
}
