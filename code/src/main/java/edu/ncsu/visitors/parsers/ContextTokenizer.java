package edu.ncsu.visitors.parsers;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
import com.github.javaparser.ast.body.TypeDeclaration;
import com.google.gson.Gson;
import com.google.gson.JsonObject;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.store.ITokenStore;
import edu.ncsu.visitors.helpers.VisitorHelper;
import edu.ncsu.mos.helpers.Contexter;

import java.util.*;
import java.util.logging.Logger;

public class ContextTokenizer {

    private final static Logger LOGGER = Logger.getLogger(ContextTokenizer.class.getName());

    private static IMetadataStore _METADATA_STORE = null;

    private static ITokenStore _TOKEN_STORE = null;

    public static IMetadataStore loadMetadataStore() {
        if (_METADATA_STORE == null)
            _METADATA_STORE = BaseStorage.loadMetadataStore(ProjectConfig.DATASET);
        return _METADATA_STORE;
    }

    public static ITokenStore loadTokenStore() {
        if (_TOKEN_STORE == null)
            _TOKEN_STORE = BaseStorage.loadTokenStore();
        return _TOKEN_STORE;
    }

    @SuppressWarnings("rawtypes")
    public static Map<String, Object> getCodeBody(String functionBody) {
        String classBody = String.format("public class SampleContextClass {\n %s \n}", functionBody);
        CompilationUnit compilationUnit = VisitorHelper.parseContent(classBody);
        for (TypeDeclaration typeDeclaration: compilationUnit.getTypes()) {
            if (!(typeDeclaration instanceof ClassOrInterfaceDeclaration))
                continue;
            for (Object met : typeDeclaration.getMethods()) {
                MethodDeclaration method = (MethodDeclaration) met;
                if (!method.getBody().isPresent())
                    continue;
                Map<String, Object> functionComponents = new HashMap<>();
                functionComponents.put("body", method.getBody().get().toString());
                functionComponents.put("name", method.getNameAsString());
                List<String> argTypes = new ArrayList<>();
                for (Parameter param: method.getParameters()) {
                    argTypes.add(param.getType().toString());
                }
                functionComponents.put("argTypes", argTypes);
                return functionComponents;
            }
        }
        return null;
    }

    private static long getHashKey(String string) {
        return string.hashCode();
    }

    public static void tokenizeDataset() {
        LOGGER.info("Fetching functions .... ");
        Map<String, JsonObject> generatedFunctionBodies = ContextTokenizer.loadMetadataStore().loadGeneratedFunctionBodies();
        int index = 0;
        System.out.println(generatedFunctionBodies.size());
        for (String name: generatedFunctionBodies.keySet()) {
            if (index % 100 == 0)
                LOGGER.info(String.format("Contextualizing function: %d / %d ... ", index + 1, generatedFunctionBodies.size()));
            JsonObject generatedFunction = generatedFunctionBodies.get(name);
            Map<String, Object> functionComponents = getCodeBody(generatedFunction.get("body").getAsString());
            String functionBody = functionComponents.get("body").toString();
            String functionName = functionComponents.get("name").toString();
            Set<String> tokens = Contexter.tokenize(functionBody);
            if (!functionName.startsWith(Settings.GENERATED_FUNCTION_PREFIX))
                tokens.addAll(Contexter.tokenize(functionName));
            if (generatedFunction.has("sourceCodeClassName")) {
                String className = generatedFunction.get("sourceCodeClassName").getAsString();
                if (!className.startsWith(Settings.GENERATED_CLASS_PREFIX) && !className.startsWith(Settings.PERMUTATED_CLASS_PREFIX))
                    tokens.addAll(Contexter.tokenize(className));
            }
            for (String argType: (ArrayList<String>) functionComponents.get("argTypes")) {
                tokens.addAll(Contexter.tokenize(argType));
            }
//            System.out.println("\n********************");
//            System.out.println(functionName);
//            System.out.println(functionBody);
//            System.out.println(tokens);
            long hashCode = getHashKey(String.join("$$", tokens));
            JsonObject functionTokenObj = new JsonObject();
            functionTokenObj.addProperty("name", name);
            functionTokenObj.addProperty("body", functionBody);
            functionTokenObj.addProperty("hash_key", hashCode);
            functionTokenObj.add("tokens", new Gson().toJsonTree(tokens).getAsJsonArray());
            ContextTokenizer.loadTokenStore().saveContextualTokens(functionTokenObj);
            index++;
        }
    }

    public static void main(String[] args) {
        tokenizeDataset();
    }

}
