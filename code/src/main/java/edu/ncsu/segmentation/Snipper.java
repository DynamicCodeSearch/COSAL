package edu.ncsu.segmentation;

import com.github.javaparser.ast.body.Parameter;
import com.google.gson.JsonObject;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.utils.JavaFormatter;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.adapters.MethodAndVariableAdapter;
import edu.ncsu.visitors.adapters.WholeMethodAdapter;
import edu.ncsu.visitors.blocks.ClassBlock;
import edu.ncsu.visitors.blocks.GeneratedFunction;
import edu.ncsu.visitors.blocks.Imports;
import edu.ncsu.visitors.blocks.MethodBlock;
import edu.ncsu.visitors.helpers.VisitorHelper;
import org.apache.commons.lang3.StringUtils;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Logger;

public class Snipper {

    private static final Logger LOGGER = Logger.getLogger(Snipper.class.getName());

    public static void generateMethodsForJavaFile(String dataset, String javaFile) {
        MethodAndVariableAdapter adapter = new MethodAndVariableAdapter(dataset, javaFile);
        List<GeneratedFunction> functions = adapter.generateMethods();
        String saveFile = saveMethods(adapter, functions);
        String packageName = VisitorHelper.getPackage(adapter.getCompilationUnit());
        String mainClassName = adapter.getMainClassName();
        saveMetaData(adapter.getDataset(), functions);
        adapter.dumpSLOCStats(functions);
        LOGGER.info(String.format("Saved %s.%s to '%s'", packageName, mainClassName, saveFile));
    }

    private static String saveMethods(MethodAndVariableAdapter adapter, List<GeneratedFunction> functions) {
        String generatedClassName = Settings.GENERATED_CLASS_PREFIX + Utils.randomString();
        String packageName = VisitorHelper.getPackage(adapter.getCompilationUnit());
        String writePath = Utils.pathJoin(Settings.PROJECTS_BASE_JAVA_FOLDER, packageName.replaceAll("\\.", File.separator));
        Utils.mkdir(writePath);
        String writeFilePath = Utils.pathJoin(writePath, generatedClassName + ".java");
        List<String> functionsAsString = new ArrayList<>();
        for (GeneratedFunction function: functions) {
            function.setSourceFile(adapter.getFileName());
            function.setGeneratedFile(writeFilePath);
            functionsAsString.add(function.getBody());
        }
        SegmentUtils.writeFunctionStringsToFile(functionsAsString, packageName, generatedClassName, writeFilePath);
        return writeFilePath;
    }

    public static List<Map<String, String>> extractMethodProps(String dataset, String javaFile, boolean skipMain) {
        MethodAndVariableAdapter adapter = new MethodAndVariableAdapter(dataset, javaFile);
        List<Map<String, String>> methodNames = new ArrayList<>();
        for (ClassBlock classBlock: adapter.getClassBlocks()) {
            for (MethodBlock methodBlock: classBlock.getMethodBlocks()) {
                Map<String, String> props = new HashMap<>();
                if (skipMain && methodBlock.getName().equals("main"))
                    continue;
                props.put("Class", classBlock.getName());
                props.put("Package", VisitorHelper.getPackage(classBlock.getCompilationUnit()));
                props.put("Method", methodBlock.getName());
                List<String> params = new ArrayList<String>();
                if (methodBlock.getMethodNode().getParameters() != null) {
                    for (Parameter param: methodBlock.getMethodNode().getParameters()) {
                        params.add(param.getType().toString() + " " + param.getNameAsString());
                    }
                }
                props.put("Args", String.format("\"%s\"", StringUtils.join(params, ";")));
                props.put("Return", methodBlock.getReturnType());
                methodNames.add(props);
            }
        }
        return methodNames;
    }

    public static void saveMetaData(String dataset, List<GeneratedFunction> generatedFunctions) {
        IMetadataStore metadataStore = BaseStorage.loadMetadataStore(dataset);
        List<JsonObject> genFuncsAsJson = new ArrayList<>();
        for (GeneratedFunction generatedFunction: generatedFunctions)
            genFuncsAsJson.add(generatedFunction.toJson());
        metadataStore.saveClassFunctionsMetadata(genFuncsAsJson);
    }

    public static void deleteMetadata(String dataset, String filePath) {
        IMetadataStore metadataStore = BaseStorage.loadMetadataStore(dataset);
        metadataStore.deleteClassFunctionsMetadata(filePath);
    }

    public static void generateWholeMethodsForJavaFile(String dataset, String javaFile) {
        WholeMethodAdapter adapter = new WholeMethodAdapter(dataset, javaFile);
        List<GeneratedFunction> generatedFunctions = adapter.getGeneratedFunctions();
        if (generatedFunctions.size() > 0) {
//            String saveFile = generatedFunctions.get(0).getGeneratedFile();
            String packageName = VisitorHelper.getPackage(adapter.getCompilationUnit());
            String mainClassName = adapter.getMainClassName();
            saveMetaData(dataset, generatedFunctions);
            LOGGER.info(String.format("Saved %d functions in DB from %s.%s", generatedFunctions.size(), packageName, mainClassName));
        }
    }

    private static void testGenerateMethods() {
        String fName = "/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/guava/src/com/google/common/base/Strings.java";
//        String fName = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Dummy/area/Stupid.java";
//        String fName = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Dummy/generics/SampleGenerics.java";
//        generateMethodsForJavaFile(ProjectConfig.DATASET, fName);
        generateWholeMethodsForJavaFile(ProjectConfig.DATASET, fName);
    }

    public static void main(String[] args) {
        testGenerateMethods();
    }

}
