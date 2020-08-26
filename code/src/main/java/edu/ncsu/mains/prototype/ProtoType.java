package edu.ncsu.mains.prototype;

import edu.ncsu.arguments.ArgumentExtractor;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.config.hyperparameters.HyperParameters;

import java.util.ArrayList;
import java.util.List;

public class ProtoType {

    public static void testFindGeneratedClass() {
//        System.out.println(PackageManager.findGeneratedClass("com.google.common.base", "permutated_class_11e3fe5a1c3146c1a3c645fbe76825fa"));
        System.out.println(PackageManager.findGeneratedClass("com.google.common.base.permutated_class_11e3fe5a1c3146c1a3c645fbe76825fa"));
    }

    public static void testFindConstants() {
        List<String> filePaths = new ArrayList<>();
        filePaths.add("/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/commons-lang/src/main/java/org/apache/commons/lang3/permutated_class_09795dd8c2a54b40b1fd40bd6db82f53.java");
        filePaths.add("/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/guava/src/com/google/common/base/permutated_class_11e3fe5a1c3146c1a3c645fbe76825fa.java");
        ArgumentExtractor extractor = new ArgumentExtractor(ProjectConfig.DATASET);
        extractor.extractAndStorePrimitiveArguments(filePaths);
    }

    public static void testFuzzedArgs() {
        boolean deleteOld = false;
        List<String> filePaths = new ArrayList<>();
        filePaths.add("/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/commons-lang/src/main/java/org/apache/commons/lang3/permutated_class_09795dd8c2a54b40b1fd40bd6db82f53.java");
//        filePaths.add("/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/guava/src/com/google/common/base/permutated_class_11e3fe5a1c3146c1a3c645fbe76825fa.java");
        ArgumentExtractor extractor = new ArgumentExtractor(ProjectConfig.DATASET);
        extractor.storeFuzzedArguments(filePaths, HyperParameters.FUZZ_ARGUMENT_SIZE, deleteOld);
    }

    public static void main(String[] args) {
        testFuzzedArgs();
    }
}
