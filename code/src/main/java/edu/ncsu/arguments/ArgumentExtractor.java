package edu.ncsu.arguments;

import edu.ncsu.config.ProjectConfig;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.executors.models.Function;
import edu.ncsu.executors.models.Primitive;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IArgumentStore;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.visitors.adapters.ConstantAdapter;

import java.util.*;
import java.util.logging.Logger;

public class ArgumentExtractor {

    private final static Logger LOGGER = Logger.getLogger(ArgumentExtractor.class.getName());

    private String dataset;

    private IArgumentStore argumentStore;

    private IMetadataStore metadataStore;

    /***
     * Initialize Argument Extractor
     * @param dataset - Name of the dataset
     */
    public ArgumentExtractor(String dataset) {
        this(dataset, false);
    }


    public ArgumentExtractor(String dataset, Boolean isTest) {
        this.dataset = dataset;
        this.metadataStore = BaseStorage.loadMetadataStore(dataset);
        this.argumentStore = BaseStorage.loadArgumentStore(dataset,isTest);
    }


    /**
     * Extract and store primitive arguments for a dataset.
     * @param javaFiles - List of paths fo java files.
     */
    public void extractAndStorePrimitiveArguments(List<String> javaFiles) {
        LOGGER.info(String.format("Number of java files: %d", javaFiles.size()));
        ConstantAdapter adapter;
        Map<Primitive, Set<Object>> constantsMap = new HashMap<>();
        Map<Primitive, Set<Object>> fileConstantsMap;
        for (String javaFile: javaFiles) {
            try {
                adapter = new ConstantAdapter(javaFile);
                fileConstantsMap = adapter.getConstantsMap();
                for(Primitive primitive: fileConstantsMap.keySet()) {
                    Set<Object> values = new HashSet<>();
                    if (constantsMap.containsKey(primitive)) {
                        values = constantsMap.get(primitive);
                    }
                    values.addAll(fileConstantsMap.get(primitive));
                    constantsMap.put(primitive, values);
                }
            } catch (Exception e) {
                LOGGER.severe(String.format("Failed to process : %s", javaFile));
                throw e;
            }
        }
        LOGGER.info("PRIOR TO SAVING !!!!");
        for (Primitive primitive: constantsMap.keySet()) {
            System.out.println(primitive + " : " + constantsMap.get(primitive).size());
        }
        this.argumentStore.savePrimitiveArguments(constantsMap);
        constantsMap = this.argumentStore.loadPrimitiveArguments();
        LOGGER.info("====================");
        LOGGER.info("POST SAVING !!!!");
        for (Primitive primitive: constantsMap.keySet()) {
            System.out.println(primitive + " : " + constantsMap.get(primitive).size());
        }
    }

    /**
     * Generate arguments and save for the java file.
     * @param javaFile - Path of the java file.
     * @parama numArgs - Number of arguments
     */
    public void generateForJavaFile(String javaFile, int numArgs) {
        ClassMethods classMethods = new ClassMethods(this.dataset, javaFile);
        classMethods.getMethods().forEach(
                (methodName, method) -> {
                    Function function = classMethods.getFunction(method.getName());
                    if (!function.isValidArgs() || function.shouldBeSkipped())
                        return;
                    function.setMetadata(metadataStore.getFunctionMetadata(function.getName()));
                    ArgumentGenerator.generateAndStoreArgumentsForFunctionIfNotExists(function, numArgs);
                }
        );
    }


    /**
     * Store fuzzed arguments for list of java files and dataset
     * @param javaFiles - List of path of java files
     */
    public void storeFuzzedArguments(List<String> javaFiles, int numArgs, boolean deleteOld) {
        LOGGER.info("Generating random args. Here we go ....");
        if (deleteOld) {
            LOGGER.info("Deleting old arguments ... ");
            argumentStore.deleteFuzzedArguments();
        } else  {
            LOGGER.info("Retaining old arguments ... ");
        }
        for (String javaFile: javaFiles) {
            LOGGER.info(String.format("Running for %s", javaFile));
            generateForJavaFile(javaFile, numArgs);
        }
    }

    private void testGenerateForJavaFile() {
//        String javaFile = "/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/guava/src/com/google/common/base/permutated_class_11e3fe5a1c3146c1a3c645fbe76825fa.java";
        String javaFile = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Dummy/area/permutated_class_a228043b7d714b73ae09b9cebd13d00b.java";
        generateForJavaFile(javaFile, 10);
    }

    public static void main(String[] args) {
        ArgumentExtractor extractor = new ArgumentExtractor(ProjectConfig.DATASET);
        extractor.testGenerateForJavaFile();
//        System.out.println("Hello World");
    }
}
