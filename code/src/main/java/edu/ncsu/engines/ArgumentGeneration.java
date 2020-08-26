package edu.ncsu.engines;

import edu.ncsu.arguments.ArgumentGenerator;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IArgumentStore;

import java.util.List;
import java.util.Map;
import java.util.logging.Logger;

public class ArgumentGeneration {

    private static final Logger LOGGER = Logger.getLogger(ArgumentGeneration.class.getName());

    public static void generateAndStoreArgumentsForKey(String functionKey, int numArgs) {
        IArgumentStore ARGUMENT_STORE = BaseStorage.loadArgumentStore(ProjectConfig.DATASET, ProjectConfig.IS_FALSE_POSITIVE_TESTING);
        if (ARGUMENT_STORE.fuzzedKeyExists(functionKey)) {
            LOGGER.info(String.format("Arguments exist for key '%s'", functionKey));
            return;
        }
        try {
            List<Map<String, List<Object>>> args = ArgumentGenerator.generateArgumentsForFunctionKey(functionKey, numArgs);
            if (args != null) {
                ARGUMENT_STORE.saveFuzzedArguments(functionKey, args);
            }
        } catch (RuntimeException e) {
            LOGGER.severe(e.getMessage());
            e.printStackTrace();
        }
        LOGGER.info("SLACC args saved successfully!!");
    }

    public static void main(String[] args) {
        if (args.length < 2) {
            LOGGER.severe("Args: <Input Key> <Num Args>");
            System.exit(0);
        }
        generateAndStoreArgumentsForKey(args[0], Integer.parseInt(args[1]));
    }

}
