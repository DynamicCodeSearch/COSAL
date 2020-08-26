package edu.ncsu.mains;

import edu.ncsu.config.ProjectConfig;
import edu.ncsu.executors.MethodExecutor;

import java.io.OutputStream;
import java.io.PrintStream;
import java.util.logging.Logger;

public class Execute {

    private static final Logger LOGGER = Logger.getLogger(Execute.class.getName());

    static {
//        System.setOut(new PrintStream(new OutputStream() {
//            @Override
//            public void write(int b) {}
//        }));

//        System.setErr(new PrintStream(new OutputStream() {
//            @Override
//            public void write(int b) {}
//        }));
    }

    public static void execute(String... args) {
        String dataset = ProjectConfig.DATASET;
        if (args.length > 0) {
            LOGGER.info(String.format("Running for problem: %s", args[0]));
            MethodExecutor.executeDatasetSerial(dataset, args[0]);
        } else {
            LOGGER.info("Running for all problems");
//            MethodExecutor.executeDataset(dataset);
            MethodExecutor.executeDatasetSerial(dataset);
        }
    }

    public static void executeFunction(String... args) {
        if (args.length < 3) {
            LOGGER.severe("First Argument: Dataset, Second Argument: FilePath, Third Argument: FunctionName");
            System.exit(0);
        }
        String dataset = args[0];
        String filePath = args[1];
        String functionName = args[2];
        MethodExecutor.executeFunction(dataset, functionName, filePath, false);
    }

    public static void reExecuteFunctions(String... args) {
        if (args.length < 1) {
            LOGGER.severe("Dataset should be the first argument");
            System.exit(0);
        }
        String dataset = args[0];
        MethodExecutor.reExecuteDataset(dataset);
    }

    public static void reExecuteFunction(String... args) {
        if (args.length < 3) {
            LOGGER.severe("First Argument: Dataset, Second Argument: FilePath, Third Argument: FunctionName");
            System.exit(0);
        }
        String dataset = args[0];
        String filePath = args[1];
        String functionName = args[2];
        MethodExecutor.executeFunction(dataset, functionName, filePath, true);
    }

    public static void main(String[] args) {
//        executeFunction("OpenSource", "/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/guava/src/com/google/common/base/permutated_class_f629e81e5afb46369170f770a39d7a87.java", "func_87ab784a2a854a0b84a3d5f41b8a2b8f");
        execute(ProjectConfig.DATASET);
    }

}
