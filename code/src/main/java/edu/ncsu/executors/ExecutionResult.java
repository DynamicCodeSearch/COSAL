package edu.ncsu.executors;

import com.google.gson.JsonObject;
import edu.ncsu.executors.helpers.FileHandler;
import edu.ncsu.executors.models.Function;

public class ExecutionResult {

    private Function function;

    private Object returnValue;

    private String errorMessage;

    private long duration;

    private int argSetIndex;

    private boolean isContentFetched = false;

    private Object _content = null;

    public Object getContent() {
        if (isContentFetched)
            return _content;
        isContentFetched = true;
        if (returnValue == null) {
            _content = null;
        } else if (FileHandler.isOutputClass(returnValue.getClass().getName())) {
            _content = FileHandler.convertFileOutput(returnValue, function.getUUID(), argSetIndex);
        } else {
            _content = returnValue;
        }
        return _content;
    }

    public Function getFunction() {
        return function;
    }

    public ExecutionResult(Function function, Object returnValue, String errorMessage, long duration, int argSetIndex) {
        this.function = function;
        this.returnValue = returnValue;
        this.errorMessage = errorMessage;
        this.duration = duration;
        this.argSetIndex = argSetIndex;
        getContent();
    }

    /***
     * Dump the execution result of the function into a JSON
     * @return - Execution result as a JSON
     */
    public JsonObject dumpReturnAsJSON() {
        int funcUUID = function.getUUID();
        JsonObject formatted = new JsonObject();
        formatted.add("return", function.formatReturnValueAsJSON(returnValue, funcUUID, argSetIndex));
        formatted.addProperty("errorMessage", errorMessage);
        formatted.addProperty("duration", duration);
        return formatted;
    }

}
