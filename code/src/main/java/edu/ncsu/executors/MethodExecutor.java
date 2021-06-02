package edu.ncsu.executors;

import com.google.common.util.concurrent.SimpleTimeLimiter;
import com.google.common.util.concurrent.TimeLimiter;
import com.google.common.util.concurrent.UncheckedTimeoutException;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import edu.ncsu.arguments.ArgumentGenerator;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.helpers.FileHandler;
import edu.ncsu.executors.helpers.ReflectionHelper;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.executors.models.Function;
import edu.ncsu.executors.models.FunctionVariable;
import edu.ncsu.executors.models.SystemClassConstructor;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IFunctionStore;
import edu.ncsu.config.hyperparameters.HyperParameters;
import edu.ncsu.utils.Utils;
import org.apache.commons.lang3.exception.ExceptionUtils;

import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.util.*;
import java.util.concurrent.*;
import java.util.logging.Logger;

public class MethodExecutor {

    private static final Logger LOGGER = Logger.getLogger(MethodExecutor.class.getName());

    private static final String METHOD_EXECUTED = "COMPLETED";

    private static Boolean ONLY_SINGLE = false;

    private static ExecutorService taskExecutor;

    private String dataset;

    private boolean isTest = false;

    private List<Function> functionsToExecute;

    private ExecutorService timeExecutor;

    private TimeLimiter timeLimiter;

    private ClassMethods classMethods;

    private IFunctionStore functionStore;

    private final static boolean DEBUG = false;

    static {
        if (taskExecutor == null || taskExecutor.isShutdown())
            taskExecutor = Executors.newFixedThreadPool(Settings.getNumCores());

        System.setOut(new PrintStream(new OutputStream() {
            @Override
            public void write(int b) {}
        }));
    }

    private void initialize() {
        if (timeExecutor == null || timeExecutor.isShutdown())
            timeExecutor = Executors.newFixedThreadPool(Settings.getNumThreads());
        if (timeLimiter == null)
            timeLimiter = new SimpleTimeLimiter(timeExecutor);
    }

    private static void shutdownExecutor(ExecutorService executorService) {
        if (executorService != null && !executorService.isShutdown()) {
            executorService.shutdownNow();
            try {
                executorService.awaitTermination(HyperParameters.METHOD_EXECUTION_WAIT_TIME, TimeUnit.MILLISECONDS);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            executorService.shutdownNow();
        }
    }

    public void shutdown() {
        if (DEBUG)
            LOGGER.info("Shutting down time executor");
        shutdownExecutor(timeExecutor);
        timeLimiter = null;
        if (DEBUG)
            LOGGER.info("Shutting down task executor");
        shutdownExecutor(taskExecutor);
    }

    private MethodExecutor(String dataset, Boolean isTest) {
        this.dataset = dataset;
        this.isTest = isTest;
        this.functionStore = BaseStorage.loadFunctionStore(dataset, isTest);
    }

    private MethodExecutor(String dataset, String sourcePath) {
        this(dataset, sourcePath, false);
    }

    private MethodExecutor(String dataset, String sourcePath, Boolean isTest) {
        this(dataset, isTest);
        LOGGER.info(dataset);
        LOGGER.info(sourcePath);
        this.classMethods = new ClassMethods(dataset, sourcePath);
        initialize();
    }

    public MethodExecutor(String dataset) {
        this.dataset = dataset;
        initialize();
    }

    /**
     * Retrieve function tasks for the Method Executor
     * @return Function Tasks for the java file
     */
    private List<Callable<Map<String, String>>> getFunctionTasks() {
        List<Callable<Map<String, String>>> functionTasks = new ArrayList<>();
        List<Function> validFunctions = getFunctionsToExecute();
        for (int i=0; i<validFunctions.size(); i++)
            functionTasks.add(makeFunctionTask(validFunctions.get(i), i));
        return functionTasks;
    }

    private List<Function> getFunctionsToExecute() {
        if (functionsToExecute != null)
            return functionsToExecute;
        LOGGER.info(String.format("Fetching functions to execute for %s.%s ...", classMethods.getPackageName(), classMethods.getClassName()));
        functionsToExecute = new ArrayList<>();
        int[] totalFunctions = new int[]{0};
        classMethods.getMethods().forEach(
                (methodName, method) -> {
                    Function function = classMethods.getFunction(method.getName());
                    if (function.isFuzzable() && function.getArgumentsKey() != null) {
                        if (!this.functionStore.isStored(function)) {
                            functionsToExecute.add(function);
                        }
                        totalFunctions[0]++;
                    }
                }
        );
        LOGGER.info(String.format("# functions to process = %d; # Valid Functions = %d; # Total Functions = %d", functionsToExecute.size(), totalFunctions[0], classMethods.getMethods().size()));
        return functionsToExecute;
    }

    /***
     * Execute a list of FunctionTask.
     * @param functionTasks - list of function tasks to execute.
     */
    private static void executeFunctionTasks(List<Callable<Map<String, String>>> functionTasks) {
        if (functionTasks == null || functionTasks.size() == 0)
            return;
        long timeToWait = functionTasks.size()
                * HyperParameters.ALL_METHOD_EXECUTIONS_WAIT_MULTIPLIER
                * HyperParameters.METHOD_EXECUTION_WAIT_TIME;
        LOGGER.info(String.format("Time to wait = %d", timeToWait));
        try {
            List<Future<Map<String, String>>> functionResults = taskExecutor.invokeAll(functionTasks, timeToWait, TimeUnit.SECONDS);
            LOGGER.info("Invoked All!");
            int toRun = functionResults.size();
            for (Future<Map<String, String>> functionResult: functionResults) {
                assert functionResult.isDone();
                Map<String, String> executionResult = functionResult.get();
                LOGGER.info("Fetched execution results");
                if (!executionResult.get("status").equals(METHOD_EXECUTED)) {
                    LOGGER.severe(String.format("Exception occurred while processing function: %s", executionResult.get("name")));
                }
                LOGGER.info(String.format("Functions remaining: %d/%d", toRun, functionResults.size()));
                --toRun;
            }
            LOGGER.info("Completed invocation");
        } catch (Exception e) {
            LOGGER.severe("Exception while invoking all function tasks");
            e.printStackTrace();
        }
        taskExecutor.shutdown();
    }


    public void process(Function function) {
        LOGGER.info(String.format("Processing function %s.%s.%s ... ",
                classMethods.getPackageName(), classMethods.getClassName(), function.getName()));
        storeFunction(function);
        LOGGER.info(String.format("Function Stored: %s", function.getName()));
    }


    private Callable<Map<String, String>> makeFunctionTask(final Function function, final int taskNumber) {
        return () -> {
            Map<String, String> retMap = new HashMap<>();
            retMap.put("name", function.getName());
            try {
                if (Settings.METHOD_EXECUTION_MODE.equals(Settings.JAVA_EXECUTION))
                    executeAsJava(function, taskNumber);
                else if (Settings.METHOD_EXECUTION_MODE.equals(Settings.BASH_EXECUTION))
                    executeAsBash(function, taskNumber);
                else
                    throw new RuntimeException(String.format("@COSAL: Invalid execution mode: '%s'", Settings.METHOD_EXECUTION_MODE));
                retMap.put("status", METHOD_EXECUTED);
            } catch (Exception e) {
                retMap.put("status", e.getMessage());
            }
            return retMap;
        };
    }

    private void executeAsBash(final Function function, final int taskNumber) {
        try {
            LOGGER.info(String.format("Submitted %s. Doing: %d / %d", function.getName(), taskNumber + 1, getFunctionsToExecute().size()));
            String scriptsFolder = Utils.pathJoin("scripts", "java");
            if (isTest)
                scriptsFolder = Utils.pathJoin(scriptsFolder, "test");
            String command = String.format("sh %s %s %s %s",
                    Utils.pathJoin(scriptsFolder, "execute_single_function.sh"),
                    dataset, classMethods.getSourcePath(), function.getName());
            Process process = Runtime.getRuntime().exec(command, Utils.getEnvs(), new File(Settings.CODE_HOME));
            process.waitFor();
            LOGGER.info(String.format("Output: %s\nError: %s\n", Utils.getOutput(process), Utils.getError(process)));
            process.destroy();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private void executeAsJava(Function function, int taskNumber) {
        try {
            LOGGER.info(String.format("Submitted %s. Doing: %d / %d", function.getName(), taskNumber + 1, getFunctionsToExecute().size()));
            process(function);
            LOGGER.info(String.format("Completed execution of %s", function.getName()));
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private void updateExecutionError(Function function, String errorTrace) {
        JsonObject failedFunction = new JsonObject();
        failedFunction.addProperty("name", function.getName());
        failedFunction.addProperty("class", function.getClassName());
        failedFunction.addProperty("package", function.getPackageName());
        failedFunction.addProperty("project", ProjectConfig.PROJECT_NAME);
        failedFunction.addProperty("errorTrace", errorTrace);
        functionStore.updateFunctionError(failedFunction);
    }

    private void storeFunction(Function function) {
        JsonObject executionResult = executeFunction(function);
        if (executionResult.has("output")) {
            JsonObject outputResult = executionResult.get("output").getAsJsonObject();
            try {
                functionStore.updateFunctionResult(outputResult);
            } catch (Exception e) {
                LOGGER.severe(String.format("Exception while saving function '%s': %s", function.getName(), e.getMessage()));
                StringWriter sw = new StringWriter();
                e.printStackTrace(new PrintWriter(sw));
                updateExecutionError(function, sw.toString());
            }
        } else if (executionResult.has("error")) {
            JsonObject error = executionResult.get("error").getAsJsonObject();
            updateExecutionError(function, error.get("errorTrace").getAsString());
        }
    }

    private JsonObject executeFunction(Function function) {
        JsonObject returnVal = new JsonObject();
        try {
            if (ONLY_SINGLE) {
                returnVal.add("output", processFunctionOnce(function));
            } else {
                returnVal.add("output", processFunction(function));
            }
        } catch (Exception e) {
            JsonObject failedFunction = new JsonObject();
            StringWriter sw = new StringWriter();
            e.printStackTrace(new PrintWriter(sw));
            failedFunction.addProperty("name", function.getName());
            failedFunction.addProperty("class", function.getClassName());
            failedFunction.addProperty("package", function.getPackageName());
            failedFunction.addProperty("project", ProjectConfig.PROJECT_NAME);
            failedFunction.addProperty("errorTrace", sw.toString());
            returnVal.add("error", failedFunction);
        }
        return returnVal;
    }


    private JsonObject processFunction(Function function) {
        List<Object[]> executionArgs = fetchFunctionExecutionArgs(function);
        if (executionArgs.size() == 0) {
            LOGGER.info(String.format("Execution args does not exist for args key: %s", function.getArgumentsKey()));
            return null;
        }
        return executeFunctionOnArgsAsJSON(function, executionArgs);
    }


    private JsonObject processFunctionOnce(Function function) {
        System.out.println(String.format("Function: %s", function.getName()));
        List<Object[]> executionArgs = fetchFunctionExecutionArgs(function);
        if (executionArgs.size() == 0) {
            LOGGER.info(String.format("Execution args does not exist for args key: %s", function.getArgumentsKey()));
            return null;
        }
        return executeFunctionOnArgsAsJSON(function, executionArgs.subList(0, 1));
    }

    public JsonObject executeFunctionOnArgsAsJSON(Function function, List<Object[]> args) {
        JsonArray executions = new JsonArray();
        int argCount = 0;
        for (Object executionArg: args) {
            executions.add(profileMethod(function, argCount, ReflectionHelper.toObjectArray(executionArg)).dumpReturnAsJSON());
            argCount += 1;
        }
        JsonObject functionData = new JsonObject();
        functionData.addProperty("name", function.getName());
        functionData.addProperty("class", function.getClassName());
        functionData.addProperty("package", function.getPackageName());
        functionData.addProperty("inputKey", function.getArgumentsKey());
        functionData.addProperty("project", ProjectConfig.PROJECT_NAME);
        functionData.add("outputs", executions);
        return functionData;
    }

    public List<ExecutionResult> executeFunctionOnArgs(Function function, List<Object[]> args) {
        List<ExecutionResult> executionResults = new ArrayList<>();
        int argCount = 0;
        for (Object executionArg: args) {
            executionResults.add(profileMethod(function, argCount, ReflectionHelper.toObjectArray(executionArg)));
            argCount += 1;
        }
        return executionResults;
    }


    private synchronized ExecutionResult profileMethod(final Function function, final int argSetIndex, final Object... executionArguments) {
        Callable<Object> methodCall = () -> {
            try {
                return function.getMethod().invoke(null, executionArguments);
            } catch (InvocationTargetException e) {
                throw new RuntimeException(e.getTargetException());
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        };
        Object returnVariable = null;
        String errorMessage = null;
        long duration = HyperParameters.METHOD_EXECUTION_WAIT_TIME;
//        long duration = Settings.METHOD_EXECUTION_WAIT_TIME * 1000;
        try {
            long startTime = System.currentTimeMillis();
            returnVariable = timeLimiter.callWithTimeout(methodCall, HyperParameters.METHOD_EXECUTION_WAIT_TIME,
                    TimeUnit.MILLISECONDS, true);
            duration = System.currentTimeMillis() - startTime;
        } catch (UncheckedTimeoutException e) {
            errorMessage = String.format("Method timed out after %d ms", HyperParameters.METHOD_EXECUTION_WAIT_TIME);
        } catch (Exception e) {
//            LOGGER.severe(ExceptionUtils.getStackTrace(e)); // TODO: Comment this out
            errorMessage = ExceptionUtils.getMessage(e);
        }
        return new ExecutionResult(function, returnVariable, errorMessage, duration, argSetIndex);
        // function.dumpReturnAsJSON(returnVariable, errorMessage, duration, argSetIndex);
    }



    private List<Object[]> fetchFunctionExecutionArgs(Function function) {
        ArgumentGenerator.generateAndStoreArgumentsForFunctionIfNotExists(function, HyperParameters.FUZZ_ARGUMENT_SIZE);
        JsonArray arguments = ArgumentGenerator.getStore().loadFuzzedArguments(function.getArgumentsKey());
        List<Object[]> functionArgs = new ArrayList<>();
        int argCount = 0;
        for (Object arg: arguments) {
            functionArgs.add(function.convertToFunctionArguments(arg, argCount).toArray());
            argCount++;
        }
        return functionArgs;
    }



    // *******************************************************************************
    // Static executor method that executes dataset, problem, function etc

    public static void executeFunction(String dataset, String functionName, String filePath, boolean isTest) {
        MethodExecutor executor = new MethodExecutor(dataset, filePath, isTest);
        LOGGER.info(String.format("Executing function '%s.%s.%s' ...", executor.classMethods.getPackageName(), executor.classMethods.getClassName(), functionName));
        Function function = executor.classMethods.getFunction(functionName);
        executor.storeFunction(function);
    }

    /**
     * Execute a dataset
     * @param dataset - Dataset to execute
     */
    public static void executeDataset(String dataset) {
        LOGGER.info(String.format("Executing methods for dataset: %s. Here we go .... ", dataset));
        String datasetPath = Settings.PROJECTS_JAVA_FOLDER;
        List<Callable<Map<String, String>>> functionTasks = new ArrayList<>();
        List<String> javaFiles = Utils.listPermutatedFiles(datasetPath);
        if (javaFiles == null || javaFiles.size() == 0) {
            javaFiles = Utils.listGeneratedFiles(datasetPath);
        }
        for (String javaFile: javaFiles) {
            MethodExecutor executor = new MethodExecutor(dataset, javaFile);
            functionTasks.addAll(executor.getFunctionTasks());
        }
        MethodExecutor.executeFunctionTasks(functionTasks);
    }

    public static void executeFolderSerial(String dataset, String folderPath) {
        List<String> javaFiles = Utils.listPermutatedFiles(folderPath);
        if (javaFiles == null || javaFiles.size() == 0) {
            javaFiles = Utils.listGeneratedFiles(folderPath);
        }
        if (javaFiles != null)
            Collections.shuffle(javaFiles);
        int javaFileCounter = 0;
        for (String javaFile: javaFiles) {
            LOGGER.info(String.format("Processing java file: '%s'. Count: %d / %d", Utils.getRepoLocalPath(javaFile), javaFileCounter + 1, javaFiles.size()) );
            LOGGER.info(String.format("Running on '%d' processors", Settings.getNumCores()));
            MethodExecutor executor = new MethodExecutor(dataset, javaFile);
            List<Function> functions = executor.getFunctionsToExecute();
            Collections.shuffle(functions);
            int functionCounter = 0;
            for (Function function: functions) {
                functionCounter++;
                if (executor.functionStore.isStored(function))
                    continue;
                LOGGER.info(String.format("Submitted %s. Doing: %d / %d", function.getName(), functionCounter, functions.size()));
                executor.storeFunction(function);
            }
            javaFileCounter++;
            executor.shutdown();
        }
    }

    public static void executeDatasetSerial(String dataset) {
        LOGGER.info(String.format("Executing methods for dataset: %s. Here we go .... ", dataset));
        executeFolderSerial(dataset, Settings.PROJECTS_JAVA_FOLDER);
    }

    public static void executeDatasetSerial(String dataset, String subFolder) {
        LOGGER.info(String.format("Executing methods for dataset: '%s' and folder '%s'. Here we go .... ", dataset, subFolder));
        executeFolderSerial(dataset, Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, subFolder));
    }

    public static void executeFile(String dataset, String javaFile) {
        LOGGER.info(String.format("Executing methods for dataset: %s and java file '%s'. Here we go .... ", dataset, javaFile));
        MethodExecutor executor = new MethodExecutor(dataset, javaFile);
        List<Callable<Map<String, String>>> functionTasks = executor.getFunctionTasks();
        MethodExecutor.executeFunctionTasks(functionTasks);
    }

    public static void reExecuteDataset(String dataset) {
        LOGGER.info(String.format("Rerunning java functions for dataset: %s", dataset));
        MethodExecutor executor = new MethodExecutor(dataset, true);
        List<String> functionNames = executor.functionStore.getExecutedFunctionNames("java");
        List<Callable<Map<String, String>>> functionTasks = new ArrayList<>();
        int index = 0;
        for (String functionName: functionNames) {
            Function function = executor.classMethods.getFunction(functionName);
            String sourceFile = executor.classMethods.getSourcePath();
            if (sourceFile == null) {
                throw new RuntimeException("Source File not found for function: " + functionName);
            }
            functionTasks.add(executor.makeFunctionTask(function, index));
            index += 1;
        }
        MethodExecutor.executeFunctionTasks(functionTasks);
    }

    private static void testFunctions() {
        String sourceFile = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Dummy/area/permutated_class_af04372d9f004f7a99842eeccb123f96.java";
        MethodExecutor executor = new MethodExecutor(ProjectConfig.DATASET, sourceFile, false);
        for (Function function: executor.getFunctionsToExecute()) {
            for (FunctionVariable fv: function.getArguments()) {
                if (fv.getSystemClassConstructor() == null)
                    continue;
                SystemClassConstructor systemClassConstructor = fv.getSystemClassConstructor();
                String constructorKey = systemClassConstructor.getJsonObject().get("key").getAsString();
                System.out.println(function.getName());
                System.out.println(String.format("%s ========= %s", fv.getName(), constructorKey));
            }
        }
    }

    private static void testExecution() {
        String sourceFile = "/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/guava/src/com/google/common/base/permutated_class_12af19636da4479b8625af5a252ae52e.java";
        String functionName = "func_bfe240d2bb724e0da8c5a2ab7cb1d48f";
        MethodExecutor executor = new MethodExecutor(ProjectConfig.DATASET, sourceFile);
        Function function = executor.classMethods.getFunction(functionName);
        executor.processFunction(function);
        executor.shutdown();
    }

    public static void main(String[] args) {
//        testFunctions();
        testExecution();
    }

}
