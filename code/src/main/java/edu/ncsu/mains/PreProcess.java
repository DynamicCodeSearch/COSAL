package edu.ncsu.mains;

import edu.ncsu.config.Settings;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.adapters.PreprocessAdapter;

import java.util.logging.Logger;

public class PreProcess {

    private static Logger LOGGER = Logger.getLogger(PreProcess.class.getName());

    public static void main(String[] args) {
        if (args.length < 1) {
            LOGGER.severe("Dataset should be the first argument");
            System.exit(0);
        }
        String dataset = args[0];
        LOGGER.info(String.format("Preprocessing '%s' dataset ... ", dataset));
        String datasetPath = Settings.PROJECTS_JAVA_FOLDER;
        for (String javaFile: Utils.listNonGeneratedJavaFiles(datasetPath)) {
            PreprocessAdapter.preprocess(javaFile);
        }
    }

}
