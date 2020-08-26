package edu.ncsu.visitors.blocks;

import com.github.javaparser.ast.Modifier;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.expr.Expression;
import com.github.javaparser.ast.type.Type;
import com.google.gson.JsonObject;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.executors.models.Primitive;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.UUID;

import static edu.ncsu.visitors.blocks.Type.*;

public class Variable {



    /**
     * Unique ID of Variable
     */
    private String uuid;

    /***
     * Access modifier of the variable
     */
    private String scope="local";

    /**
     * Type of variable
     */
    protected String type;

    /**
     * AST Type of variable
     */
    protected Type astType;

    /**
     * Name of package
     */
    protected String packageName;

    /**
     * Name of variable
     */
    protected String name;

    /**
     * Number of dimensions of array
     */
    protected Integer arrayDimensions;

    /**
     * Initial value of Variable
     */
    protected Expression initValue = null;

    /**
     * Start postiion variable was declared
     */
    protected VariablePosition startPosition;

    /**
     * Positions where variables used
     */
    protected List<VariablePosition> usedPositions;

    /***
     * Positions where variables had their values changed
     */
    protected List<VariablePosition> assignPositions;

    /**
     * End scope of variable
     */
    protected Integer endScopeLineNumber;

    /**
     * Modifier code of the variable
     */
    protected List<Modifier> modifiers;

    /**
     * @return Type(AST) of variable
     */
    public Type getAstType() {
        return astType;
    }

    /**
     * @return Type(String) of variable
     */
    public String getType() {
        return type;
    }

    /**
     * @return Name of variable
     */
    public String getName() {
        return name;
    }


    public VariablePosition getStartPosition() {
        return startPosition;
    }

    /**
     * @return Line where variable's scope ends
     */
    public Integer getEndScopeLineNumber() {
        return endScopeLineNumber;
    }

    /**
     * @param position Insert position of variable
     */
    public void insertUsedPosition(VariablePosition position) {
        if (usedPositions == null)
            usedPositions = new ArrayList<>();
        usedPositions.add(position);
    }

    public void insertAssignPosition(VariablePosition position) {
        if (assignPositions == null)
            assignPositions = new ArrayList<>();
        assignPositions.add(position);
    }

    /**
     * @return The number of dimensions in the array
     */
    public Integer getArrayDimensions() {
        return arrayDimensions;
    }

    public List<Modifier> getModifiers() {
        return modifiers;
    }

    /**
     * Set the arrayDimensions for the variable
     * @param arrayDimensions The dimensions of variable
     */
    public void setArrayDimensions(int arrayDimensions) {
        this.arrayDimensions = arrayDimensions;
    }

    /**
     * Create a new variable
     * @param name Name of the variable
     * @param type Type of the variable
     * @param lineNumber Line number where variable was declared.
     * @param columnNumber Column number where variable was declared.
     */
    public Variable(String name, String type, Integer lineNumber, Integer columnNumber) {
        this.uuid = UUID.randomUUID().toString();
        this.name = name;
        this.type = type;
        if (lineNumber != null && columnNumber != null) {
            this.startPosition = new VariablePosition(lineNumber, columnNumber);
        }
    }

    /**
     * Create a new variable
     * @param name Name of the variable
     * @param type Type of the variable
     * @param lineNumber Line number where variable was declared.
     * @param columnNumber Column number where variable was declared.
     * @param initValue Initial value of variable
     */
    public Variable(String name, String type, Integer lineNumber, Integer columnNumber, Expression initValue) {
        this(name, type, lineNumber, columnNumber);
        this.initValue = initValue;
    }

    /**
     * Create a new variable
     * @param name Name of the variable
     * @param type Type of the variable
     * @param lineNumber Line number where variable was declared.
     * @param columnNumber Column number where variable was declared.
     * @param initValue Initial value of variable
     * @param parentNode AST of block where variable was declared
     */
    public Variable(String name, String type, Integer lineNumber, Integer columnNumber, Expression initValue, Node parentNode) {
        this(name, type, lineNumber, columnNumber, initValue);
        this.endScopeLineNumber = parentNode.getEnd().map(position -> position.line - 1).orElse(null);
    }

    /**
     * Create a new variable
     * @param name Name of the variable
     * @param type Type of the variable
     * @param lineNumber Line number where variable was declared.
     * @param columnNumber Column number where variable was declared.
     * @param initValue Initial value of variable
     * @param parentNode AST of block where variable was declared
     */
    public Variable(String name, Type type, Integer lineNumber, Integer columnNumber, Expression initValue,
                    Node parentNode) {
        this(name, type.getElementType().asString(), lineNumber, columnNumber, initValue, parentNode);
        this.astType = type;
        this.arrayDimensions = type.getArrayLevel();
    }

    public Variable(String name, Type type, Integer lineNumber, Integer columnNumber, Expression initValue,
                    Node parentNode, List<Modifier> modifiers) {
        this(name, type, lineNumber, columnNumber, initValue, parentNode);
        this.modifiers = modifiers;
    }


    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Variable))
            return false;
        Variable other = (Variable) obj;
        return this.uuid.equals(other.uuid);
    }

    @Override
    public int hashCode() {
        return this.uuid.hashCode();
    }

    @Override
    public String toString() {
        return this.type + "$$" + this.name + "$$" + this.startPosition;
    }

    public String toTypeString() {
        StringBuilder typeString = new StringBuilder();
        if (Primitive.isValidType(type)) {
            if (Primitive.isBoxed(type))
                typeString.append(Primitive.getBoxedName(Primitive.getPrimitive(type)));
            else
                typeString.append(Primitive.getUnboxedName(Primitive.getPrimitive(type)));
        } else {
            typeString.append(type);
        }
        for (int i=0; i<this.arrayDimensions; i++)
            typeString.append("[]");
        return typeString.toString();
    }

    public String toFunctionParameter() {
        return String.format("%s %s", toTypeString(), getName());
    }

    public boolean isAssignedInRange(VariablePosition start, VariablePosition end) {
        if (assignPositions == null || assignPositions.size() == 0)
            return false;
        for (VariablePosition assignedPosition: assignPositions) {
            if (assignedPosition.isOnOrAfter(start) && assignedPosition.isOnOrBefore(end))
                return true;
        }
        return false;
    }

    public boolean isMutable() {
        return !(IMMUTABLES.contains(type));
    }

    public static class VariableComparator implements Comparator<Variable> {
        @Override
        public int compare(Variable o1, Variable o2) {
            Primitive o1Primitive = Primitive.isValidType(o1.type) ? Primitive.getPrimitive(o1.type) : null;
            Primitive o2Primitive = Primitive.isValidType(o2.type) ? Primitive.getPrimitive(o2.type) : null;
            if (o1Primitive != null && o2Primitive != null) {
                if (o1Primitive.getIndex() == o2Primitive.getIndex()) {
                    return Integer.compare(o1.arrayDimensions, o2.arrayDimensions);
                } else {
                    return Integer.compare(o1Primitive.getIndex(), o2Primitive.getIndex());
                }
            } else if (o1Primitive != null) {
                return -1;
            } else if (o2Primitive != null) {
                return 1;
            } else {
                if (o1.type.equals(o2.type)) {
                    return Integer.compare(o1.arrayDimensions, o2.arrayDimensions);
                } else {
                    return o1.type.compareTo(o2.type);
                }
            }
        }
    }

}
