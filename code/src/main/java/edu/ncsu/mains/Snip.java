package edu.ncsu.mains;

import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.segmentation.SnipFilter;
import edu.ncsu.segmentation.Snipper;
import edu.ncsu.utils.MavenUtils;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.adapters.MethodAndVariableAdapter;

import java.util.Arrays;
import java.util.Collections;
import java.util.logging.Logger;

public class Snip {

    private static Logger LOGGER = Logger.getLogger(Snip.class.getName());


    private static void snipDataset() {
        String dataset = ProjectConfig.DATASET;
        LOGGER.info(String.format("Processing for Dataset: %s", dataset));
        String datasetPath = Settings.PROJECTS_JAVA_FOLDER;
        snipFolder(datasetPath);
        MavenUtils.buildProject();
    }


    private static void snipProblem(String problem) {
        String dataset = ProjectConfig.DATASET;
        LOGGER.info(String.format("Processing for Dataset: %s and Problem: %s", dataset, problem));
        String problemPath = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, problem);
        snipFolder(problemPath);
        MavenUtils.buildProject();
    }

    private static void snipFolder(String folderPath) {
        String dataset = ProjectConfig.DATASET;
        for (String generatedFile: Utils.listFilesWithExtension(folderPath, ".java", true, true, Arrays.asList(Settings.PERMUTATED_CLASS_PREFIX, Settings.GENERATED_CLASS_PREFIX))) {
            Snipper.deleteMetadata(dataset, Utils.getRepoLocalPath(generatedFile));
            Utils.deleteFileOrFolder(generatedFile);
        }
        for (String javaFile: Utils.listNonGeneratedJavaFiles(folderPath)) {
            Snipper.generateMethodsForJavaFile(dataset, javaFile);
        }
    }

    public static void filterDataset() {
        LOGGER.info(String.format("Filtering generated files for dataset: '%s'", ProjectConfig.DATASET));
        MavenUtils.buildProject();
        String datasetPath = Settings.PROJECTS_JAVA_FOLDER;
        filterFolder(datasetPath);
        MavenUtils.buildProject();
    }

    private static void filterFolder(String folderPath) {
        for (String generatedFile: Utils.listGeneratedFiles(folderPath)) {
            SnipFilter.filterFile(generatedFile);
        }
    }

    public static void testSnip() {
//        snipDataset();
        Snipper.generateMethodsForJavaFile(ProjectConfig.DATASET, "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Dummy/area/Stupid.java");
    }

    public static void main(String[] args) {
//        filterDataset();
//        testSnip();
//        System.exit(0);
        if (args.length > 0) {
            String problem = args[0];
            snipProblem(problem);
        } else {
            snipDataset();
        }
    }

}
