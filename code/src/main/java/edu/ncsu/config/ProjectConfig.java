package edu.ncsu.config;

import edu.ncsu.config.project.*;
import edu.ncsu.utils.Utils;
import sun.reflect.generics.reflectiveObjects.NotImplementedException;

public class ProjectConfig {

    /**
     * Home path
     */
    public final static String HOME = System.getenv("HOME");

    /**
     * Parent folder of the main project source code
     */
    public final static String ROOT_PATH = Utils.pathJoin(HOME, "Raise", "ProgramRepair");

    /**
     * Project main folder. Includes source code(code), codejam projects(projects) etc.
     */
    public final static String CODESEER_HOME = Utils.pathJoin(ROOT_PATH, "CodeSeer");


    private final static BaseProjectConfig LOCAL_CONFIG = getProjectConfig();

    /**
     * Return the current ProjectConfig
     * @return Project config based on configuration.
     */
    private static BaseProjectConfig getProjectConfig() {
        String config = CodeSeerProperties.getProperties("config");
        switch (config) {
            case "dummy":
                return new DummyConfig();
            case "codejam":
                return new CodeJamConfig();
            case "introclass":
                return new IntroClassConfig();
            case "apache":
                return new ApacheConfig();
            case "guava":
                return new GuavaConfig();
            case "atcoder-methods":
                return new AtCoderMethodConfig();
            default:
                throw new RuntimeException(String.format("@COSAL: Invalid configuration: '%s'", config));
        }
    }

    /***
     * Name of the project
     */
    public final static String PROJECT_NAME = LOCAL_CONFIG.getProjectName();

    /***
     * Name of the dataset. Also name of the mongo database
     */
    public final static String DATASET = LOCAL_CONFIG.getDataset();

    /***
     * Name of the jar.
     */
    public final static String JAR_NAME = LOCAL_CONFIG.getJarName();

    /***
     * Relative path to java folder. Most projects have it as  'src/main/java'
     */
    public final static String JAVA_FOLDER = LOCAL_CONFIG.getJavaFolder();

    /**
     * Local project folders
     */
    public final static String TARGET_SOURCE = Utils.pathJoin(CODESEER_HOME, LOCAL_CONFIG.getTargetSource());

    /**
     * Local dataset folders
     */
    public final static String DATASET_JAVA_FOLDER = Utils.pathJoin(CODESEER_HOME, LOCAL_CONFIG.getDatasetFolder());

    /**
     * Path to project java folders
     */
    public final static String PROJECTS_JAVA_FOLDER = Utils.pathJoin(CODESEER_HOME, LOCAL_CONFIG.getProjectsJavaFolder());

    /**
     * Path to POM
     */
    public final static String POM_PATH = Utils.pathJoin(CODESEER_HOME, LOCAL_CONFIG.getPomPath());

    /**
     * Path to built JAR
     */
    public final static String JAR_PATH = Utils.pathJoin(CODESEER_HOME, LOCAL_CONFIG.getJarPath());

    /**
     * If true the argument generation is changed to a different store
     */
    public final static boolean IS_FALSE_POSITIVE_TESTING = Boolean.parseBoolean(CodeSeerProperties.getProperties("fp_testing"));

    /**
     * @return - Absolute path to folder with seed inputs.
     */
    public static String getSeedFileInputsFolder() {
        try {
            return Utils.pathJoin(CODESEER_HOME, LOCAL_CONFIG.getSeedFileInputsFolder());
        } catch (NotImplementedException e) {
            throw new RuntimeException(String.format("Method `getSeedFileInputsFolder` is not implemented for config: '%s'", CodeSeerProperties.getProperties("config")));
        }
    }

}
