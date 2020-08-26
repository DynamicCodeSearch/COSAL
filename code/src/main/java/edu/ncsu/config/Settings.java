package edu.ncsu.config;

import edu.ncsu.codejam.CodejamUtils;
import edu.ncsu.introclass.IntroClassUtils;
import edu.ncsu.utils.Utils;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class Settings {

    public final static boolean DEBUG = false;

    // File Paths

    /**
     * Source code folder
     */
    public static String CODE_HOME = Utils.pathJoin(ProjectConfig.CODESEER_HOME, "code");

    /**
     * Projects folder
     */
    public static String PROJECTS_HOME = ProjectConfig.TARGET_SOURCE;

    /**
     * Java folder
     */
    public static String SRC_MAIN_JAVA = ProjectConfig.JAVA_FOLDER;

    /***
     *
     */
    public static String PROJECTS_BASE_JAVA_FOLDER = Utils.pathJoin(PROJECTS_HOME, SRC_MAIN_JAVA);

    /**
     * Folder for projects/src/main/java/<dataset>
     */
    public static String PROJECTS_JAVA_FOLDER = ProjectConfig.PROJECTS_JAVA_FOLDER;

    public static String PROJECTS_JAR_PATH = Utils.pathJoin(CODE_HOME, "jars", ProjectConfig.JAR_NAME);

    public final static String JDK_JAR_PATH = Utils.pathJoin(CODE_HOME, "jars", "Java8.jar");

    public final static String JDK_SOURCE_PATH = Utils.pathJoin(ProjectConfig.ROOT_PATH, "Java8");

    /**
     * Meta-store folder
     */
    public static String META_STORE = Utils.pathJoin(CODE_HOME, "meta_store");

    /**
     * Meta-results folder
     */
    public static String META_RESULTS = Utils.pathJoin(CODE_HOME, "meta_results");

    public static String META_RESULTS_SLOC = Utils.pathJoin(META_RESULTS, "sloc");

    /**
     * Resources folder
     */
    public static String CODE_RESOURCES_FOLDER = Utils.pathJoin(CODE_HOME, "src", "main", "resources");

    public static String CONFIG_FILE_PATH = Utils.pathJoin(CODE_HOME, "src", "main", "resources", "config.properties");


    // ************************************************************************************** //


    // Constants



    /**
     * Generated class prefix
     */
    public static String GENERATED_CLASS_PREFIX = "generated_class_";

    /**
     * Generated class prefix
     */
    public static String PERMUTATED_CLASS_PREFIX = "permutated_class_";

    /**
     * Generated function prefix
     */
    public static String GENERATED_FUNCTION_PREFIX = "func_";

    /**
     * Temporary class prefix
     */
    public static String TEMPORARY_CLASS_PREFIX = "temp_class_";

    /**
     * Number of threads for execution
     */
    public static int NUM_THREADS = 1;

    /**
     * Mongo storage
     */
    public final static String MONGO_STORAGE = "mongo";

    /**
     * Json storage
     */
    public final static String JSON_STORAGE = "json";

    /**
     * Execution as java
     */
    public final static String JAVA_EXECUTION = "java";

    /**
     * Execution as bash
     */
    public final static String BASH_EXECUTION = "bash";

    /**
     * Java Language
     */
    public final static String LANGUAGE_JAVA = "java";

    /**
     * Python Language
     */
    public final static String LANGUAGE_PYTHON = "py";

    /**
     * Execution mode for methodsß
     */
    public final static String METHOD_EXECUTION_MODE = JAVA_EXECUTION;


    // ************************************************************************************** //

    // Some property based functions

    public static String getObjectStore(String dataset) {
        return Utils.pathJoin(META_STORE, dataset, "classes.json");
    }

    public static String getMetaResultsFunctionsFolder(String dataset) {
        return Utils.pathJoin(META_RESULTS, dataset, "functions");
    }

    public static String getDatasetSourceFolder(String dataset) {
        if (dataset.equals(CodejamUtils.DATASET) || dataset.equals(IntroClassUtils.DATASET))
            return PROJECTS_JAVA_FOLDER;
        throw new RuntimeException(String.format("Illegal dataset: %s", dataset));
    }

    public static String getProperty(String property) {
        Properties properties = new Properties();
        InputStream stream;
        try {
            stream = new FileInputStream(CONFIG_FILE_PATH);
            properties.load(stream);
            return properties.getProperty(property);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static String getScriptsFolder(String dataset) {
        if (dataset.equals(CodejamUtils.DATASET))
            return Utils.pathJoin("scripts", "codejam", "java");
        else if (dataset.equals(IntroClassUtils.DATASET))
            return Utils.pathJoin("scripts", "introclass");
        throw new RuntimeException(String.format("Illegal dataset: %s", dataset));
    }

    public static int getNumThreads() {
        String storage = getProperty("store");
        if (storage.equals(MONGO_STORAGE)) {
            return 8 * NUM_THREADS;
        } else if (storage.equals(JSON_STORAGE)) {
            return NUM_THREADS;
        }
        throw new RuntimeException(String.format("Unknown store: %s", storage));
    }

    public static int getNumCores() {
        return Runtime.getRuntime().availableProcessors();
    }

}
