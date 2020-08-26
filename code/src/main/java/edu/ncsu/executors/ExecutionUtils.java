package edu.ncsu.executors;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import edu.ncsu.arguments.ArgumentGenerator;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.hyperparameters.HyperParameters;
import edu.ncsu.executors.models.Function;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IFunctionStore;

import java.io.PrintWriter;
import java.io.StringWriter;
import java.util.ArrayList;
import java.util.List;

public class ExecutionUtils {

    private static MethodExecutor METHOD_EXECUTOR = null;

    private static IFunctionStore FUNCTION_STORE = BaseStorage.loadFunctionStore(ProjectConfig.DATASET, false);

    public static List<Object[]> loadArguments(Function function, int argLimit) {
        ArgumentGenerator.generateAndStoreArgumentsForFunctionIfNotExists(function, HyperParameters.FUZZ_ARGUMENT_SIZE);
        JsonArray arguments = ArgumentGenerator.getStore().loadFuzzedArguments(function.getArgumentsKey());
        if (arguments == null)
            return null;
        List<Object[]> functionArgs = new ArrayList<>();
        int argCount = 0;
        for (Object arg: arguments) {
            functionArgs.add(function.convertToFunctionArguments(arg, argCount).toArray());
            if (argLimit > 0 && functionArgs.size() == argLimit)
                break;
            argCount += 1;
        }
        return functionArgs;
    }

    public static MethodExecutor getMethodExecutor() {
        if (METHOD_EXECUTOR == null)
            METHOD_EXECUTOR = new MethodExecutor(ProjectConfig.DATASET);
        return METHOD_EXECUTOR;
    }


    public static List<ExecutionResult> executeFunction(Function function, List<Object[]> executionArgs) {
        return getMethodExecutor().executeFunctionOnArgs(function, executionArgs);
    }

    public static JsonObject executeFunctionAsJSON(Function function, List<Object[]> executionArgs) {
        JsonObject functionData = new JsonObject();
        functionData.addProperty("name", function.getName());
        functionData.addProperty("class", function.getClassName());
        functionData.addProperty("package", function.getPackageName());
        functionData.addProperty("inputKey", function.getArgumentsKey());
        functionData.addProperty("project", ProjectConfig.PROJECT_NAME);
        try {
            JsonArray executions = new JsonArray();
            List<ExecutionResult> executionResults = executeFunction(function, executionArgs);
            for (ExecutionResult executionResult: executionResults)
                executions.add(executionResult.dumpReturnAsJSON());
            functionData.add("outputs", executions);
            return functionData;
        } catch (Exception e) {
            StringWriter sw = new StringWriter();
            e.printStackTrace(new PrintWriter(sw));
            functionData.addProperty("errorTrace", sw.toString());
        }
        return functionData;
    }

    public static void storeFunction(JsonObject executedFunction) {
        if (executedFunction.has("outputs")) {
            FUNCTION_STORE.updateFunctionResult(executedFunction);
        } else if (executedFunction.has("errorTrace")) {
            FUNCTION_STORE.updateFunctionError(executedFunction);
        }
    }

    public static void shutdownExecutor() {
        if (METHOD_EXECUTOR != null)
            METHOD_EXECUTOR.shutdown();
        METHOD_EXECUTOR = null;
    }
}
