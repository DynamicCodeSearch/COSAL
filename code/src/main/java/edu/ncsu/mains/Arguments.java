package edu.ncsu.mains;

import edu.ncsu.arguments.ArgumentExtractor;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.config.hyperparameters.HyperParameters;
import edu.ncsu.utils.Utils;

import java.util.List;

public class Arguments {

    private static List<String> listOriginalFiles() {
        String datasetPath = Settings.PROJECTS_JAVA_FOLDER;
        return Utils.listNonGeneratedJavaFiles(datasetPath);
    }

    public static void extractAndStorePrimitiveArguments() {
        String dataset = ProjectConfig.DATASET;
        List<String> javaFiles = listOriginalFiles();
        ArgumentExtractor extractor = new ArgumentExtractor(dataset);
        extractor.extractAndStorePrimitiveArguments(javaFiles);
    }

    public static void storeFuzzedArguments(String... args) {
        String dataset = ProjectConfig.DATASET;
        boolean deleteOld = false;
        if (args.length > 0) {
            deleteOld = Boolean.parseBoolean(args[0].toLowerCase().trim());
        }
        List<String> javaFiles = Utils.listPermutatedFiles(Settings.PROJECTS_JAVA_FOLDER);
        if (javaFiles == null || javaFiles.size() == 0)
            javaFiles = Utils.listGeneratedFiles(Settings.PROJECTS_JAVA_FOLDER);
        ArgumentExtractor extractor = new ArgumentExtractor(dataset);
        extractor.storeFuzzedArguments(javaFiles, HyperParameters.FUZZ_ARGUMENT_SIZE, deleteOld);
    }

    public static void storeTestFuzzedArguments() {
        String dataset = ProjectConfig.DATASET;
        List<String> javaFiles = Utils.listPermutatedFiles(Settings.PROJECTS_JAVA_FOLDER);
        if (javaFiles == null || javaFiles.size() == 0)
            javaFiles = Utils.listGeneratedFiles(Settings.PROJECTS_JAVA_FOLDER);
        ArgumentExtractor extractor = new ArgumentExtractor(dataset, true);
        extractor.storeFuzzedArguments(javaFiles, HyperParameters.TEST_FUZZ_ARGUMENT_SIZE, true);
    }

    public static void main(String[] args) {
        extractAndStorePrimitiveArguments();
    }

}
