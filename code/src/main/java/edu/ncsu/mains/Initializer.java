package edu.ncsu.mains;

import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.utils.MavenUtils;
import edu.ncsu.utils.Utils;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.logging.Logger;

public class Initializer {

    private static Logger LOGGER = Logger.getLogger(Initializer.class.getName());

    public static void initializeDataset() {
        String dataset = ProjectConfig.DATASET;
        LOGGER.info(String.format("Initializing dataset: '%s'.", dataset));

        // Clear meta_results/dataset
        LOGGER.info(String.format("Clearing meta results for dataset: '%s' ... ", dataset));
        Utils.deleteFileOrFolder(Utils.pathJoin(Settings.META_RESULTS, dataset));
        Utils.deleteFileOrFolder(Utils.pathJoin(Settings.META_RESULTS_SLOC, dataset));

        // Clear meta_store/dataset
        LOGGER.info(String.format("Clearing meta store for dataset: '%s' ... ", dataset));
        Utils.deleteFileOrFolder(Utils.pathJoin(Settings.META_STORE, dataset));

        // Delete generated, permutated, temp files
        LOGGER.info(String.format("Deleting generated files for dataset: '%s' ... ", dataset));
        deleteGeneratedFiles(ProjectConfig.DATASET_JAVA_FOLDER);

        // Drop database
        LOGGER.info(String.format("Dropping database for dataset: '%s' ... ", dataset));
        BaseStorage.loadCommonStore().clearStoreForDataset();
        BaseStorage.loadCommonStore().initializeDataset();

        // Initializing Project
        initializeProject();
    }

    private static void deleteGeneratedFiles(String folderPath) {
        List<String> prefixes = Arrays.asList(Settings.PERMUTATED_CLASS_PREFIX, Settings.GENERATED_CLASS_PREFIX, Settings.TEMPORARY_CLASS_PREFIX);
        List<String> generatedFiles = Utils.listFilesWithExtension(folderPath, ".java",true, true, prefixes);
        Utils.deleteFilesOrFolders(generatedFiles);
    }

    public static void initializeProject() {
        String dataset = ProjectConfig.DATASET;
        String projectName = ProjectConfig.PROJECT_NAME;
        LOGGER.info(String.format("Initializing dataset: '%s', project: %s.", dataset, projectName));

        // Delete generated, permutated, temp files
        LOGGER.info(String.format("Deleting generated files for dataset: '%s', project: '%s' ... ", dataset, projectName));
        deleteGeneratedFiles(ProjectConfig.PROJECTS_JAVA_FOLDER);

        // Delete documents from database
        LOGGER.info(String.format("Dropping database for dataset: '%s', project: '%s' ... ", dataset, projectName));
        BaseStorage.loadCommonStore().clearStoreForProject();

        // Build project and copy in Jars folder
        LOGGER.info(String.format("Building project for dataset: '%s', project: '%s' ... ", dataset, projectName));
        MavenUtils.buildProject();

    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(args));
        if (args.length < 1) {
            LOGGER.severe("First argument should be 'dataset' or 'project'!");
            System.exit(0);
        }
        switch (args[0]) {
            case "dataset":
                initializeDataset();
                break;
            case "project":
                initializeProject();
                break;
            default:
                LOGGER.severe("First argument should be 'dataset' or 'project'!");
        }
    }

}
