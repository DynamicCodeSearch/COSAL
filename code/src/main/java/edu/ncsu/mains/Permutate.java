package edu.ncsu.mains;

import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.segmentation.Permutator;
import edu.ncsu.utils.MavenUtils;
import edu.ncsu.utils.Utils;

import java.util.logging.Logger;

public class Permutate {

    private static Logger LOGGER = Logger.getLogger(Snip.class.getName());

    private static final boolean FORCE_PERMUTATE = true;

    public static void permutateDataset() {
        String dataset = ProjectConfig.DATASET;
        LOGGER.info(String.format("Processing for Dataset: %s", dataset));
        String datasetPath = Settings.PROJECTS_JAVA_FOLDER;
        permutateFolder(datasetPath);
        MavenUtils.buildProject();
    }

    private static void permutateFolder(String folderPath) {
        String dataset = ProjectConfig.DATASET;
        for (String javaFile : Utils.listGeneratedFiles(folderPath)) {
            LOGGER.info(String.format("Processing file: %s. ...", javaFile));
            Permutator.permutateFile(dataset, javaFile, FORCE_PERMUTATE);
        }
    }

    public static void main(String[] args) {
        permutateDataset();
    }

}
