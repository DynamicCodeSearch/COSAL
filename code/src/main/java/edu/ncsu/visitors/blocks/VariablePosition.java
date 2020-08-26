package edu.ncsu.visitors.blocks;

import com.github.javaparser.Position;

public class VariablePosition extends Position{
    /**
     * @param line Line number
     * @param column Column number
     */
    public VariablePosition(Integer line, Integer column) {
        super(line, column);
    }

    /**
     * @return line number
     */
    public Integer getLine() {
        return line;
    }

    /**
     * @return column index
     */
    public Integer getColumn() {
        return column;
    }

    /**
     * @param other Instance of Variable
     * @return True if variable is on or after the current variable
     */
    public boolean isOnOrAfter(VariablePosition other) {
        return this.getLine() >= other.getLine() ||
                (this.getLine().equals(other.getLine()) && this.getColumn() >= other.getColumn());
    }

    /**
     * @param other Instance of Variable
     * @return True if variable is after the current variable
     */
    public boolean isOnOrBefore(VariablePosition other) {
        return this.getLine() <= other.getLine() ||
                (this.getLine().equals(other.getLine()) && this.getColumn() <= other.getColumn());
    }


    @Override
    public String toString() {
        return String.format("%d : %d", this.getLine(), this.getColumn());
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof VariablePosition))
            return false;
        VariablePosition other = (VariablePosition) obj;
        return this.getLine().equals(other.getLine()) && this.getColumn().equals(other.getColumn());
    }

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 31 * hash + this.getLine();
        hash = 31 * hash + this.getColumn();
        return hash;
    }

}
