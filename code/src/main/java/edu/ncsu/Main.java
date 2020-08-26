package edu.ncsu;

import edu.ncsu.mains.*;
import edu.ncsu.mains.prototype.ProtoType;

import java.util.Arrays;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {

    private static final Logger LOGGER = Logger.getLogger(Main.class.getName());

    public static void main(String[] args) {
        if (args.length < 1) {
            LOGGER.log(Level.SEVERE, String.format("Size of arguments is less than 1. Arguments = %s",
                    Arrays.toString(args)));
        } else {
            switch (args[0]) {
                case "mos":
                    // All for Multiobjective search
                    edu.ncsu.mos.Main.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "initialize":
                    Initializer.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "crawl":
                    Crawler.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "preprocess":
                    PreProcess.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "snip":
                    Snip.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "filter":
                    Snip.filterDataset();
                    break;
                case "permutate":
                    Permutate.permutateDataset();
                    break;
                case "dead_code":
                    DeadCode.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "extract_primitive_args":
                    Arguments.extractAndStorePrimitiveArguments();
                    break;
                case "extract_fuzzed_args":
                    Arguments.storeFuzzedArguments(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "execute":
                    Execute.execute(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "execute_single":
                    // TODO: Change path of script and MethodExecutor.java to independent of dataset
                    Execute.executeFunction(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "test_prototype":
                    ProtoType.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                // For Validating clusters
                case "test_extract_fuzzed_args":
                    Arguments.storeTestFuzzedArguments();
                    break;
                case "test_reexecute_functions":
                    Execute.reExecuteFunctions(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "test_reexecute_single":
                    Execute.reExecuteFunction(Arrays.copyOfRange(args, 1, args.length));
                    break;
                // Scratch Pad
                case "scratch":
                    ScratchPad.main(args);
                    break;
                // Engines
                // Execution Engine
                case "engine_execution":
                    edu.ncsu.engines.Execution.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "argument_engine":
                    edu.ncsu.engines.ArgumentGeneration.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                default:
                    LOGGER.log(Level.SEVERE, String.format("WTF!! Illegal argument '%s'", args[0]));
                    break;
            }
        }
    }

}
