package edu.ncsu.executors.models;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.TypeDeclaration;
import com.google.gson.JsonObject;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.utils.ParserUtils;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ClassMethods {

    private String dataset;

    private String sourcePath;

    private String className;

    private String packageName;

    private Map<String, Method> methods;

    private Map<String, Function> functions;

    private IMetadataStore metadataStore;

    private Map<String, MethodDeclaration> methodBodies;

    public Map<String, Method> getMethods() {
        return methods;
    }

    public Map<String, MethodDeclaration> getMethodBodies() {
        if (methodBodies != null)
            return methodBodies;
        methodBodies = new HashMap<>();
        functions = new HashMap<>();
        CompilationUnit compilationUnit = VisitorHelper.loadCompilationUnit(VisitorHelper.parseFile(sourcePath));
        TypeDeclaration classObject = compilationUnit.getTypes().get(0);
        for (Object member: classObject.getMembers()) {
            if (member instanceof MethodDeclaration) {
                MethodDeclaration method = (MethodDeclaration) member;
                methodBodies.put(method.getNameAsString(), method);
            }
        }
        return methodBodies;
    }

    @SuppressWarnings("rawtypes")
    public ClassMethods(String dataset, String sourcePath) {
        this.dataset = dataset;
        this.sourcePath = sourcePath;
        this.metadataStore = BaseStorage.loadMetadataStore(dataset);
        ParserUtils parserUtils = new ParserUtils(sourcePath);
        String classKey = parserUtils.makeKey();
        Class clazz = PackageManager.findGeneratedClass(classKey);
        this.packageName = clazz.getPackage().getName();
        this.className = clazz.getSimpleName();
        methodBodies = getMethodBodies();
        methods = new HashMap<>();
        if (clazz != null) {
            for (Method method: clazz.getDeclaredMethods()) {
                if (method.getName().startsWith(Settings.GENERATED_FUNCTION_PREFIX)
                        && methodBodies.containsKey(method.getName()))
                    methods.put(method.getName(), method);
            }
        }

    }

    public MethodDeclaration getMethodBody(String name) {
        return getMethodBodies().get(name);
    }

    public Function getFunction(String methodName) {
        if (functions.containsKey(methodName))
            return functions.get(methodName);
        Method method = methods.get(methodName);
        MethodDeclaration ast = getMethodBody(methodName);
        Function function = new Function(this.dataset, method, ast, this.sourcePath);
        JsonObject metadata = this.metadataStore.getFunctionMetadata(function.getName());
        if (metadata == null)
            return null;
        function.setMetadata(metadata);
        functions.put(methodName, function);
        return function;
    }

    public Map<String, Function> getFilteredFunctions() {
        Map<String, Function> filteredFunctions = new HashMap<>();
        Map<String, Object> query = new HashMap<>();
        query.put("filePath", Utils.getRepoLocalPath(this.sourcePath));
        query.put("isFiltered", true);
        Map<String, JsonObject> jsonObjects = this.metadataStore.getFunctionsMetadata(query);
        jsonObjects.forEach((methodName, metadata) -> {
            Method method = methods.get(methodName);
            MethodDeclaration ast = getMethodBody(methodName);
            Function function = new Function(this.dataset, method, ast, this.sourcePath);
            function.setMetadata(metadata);
            this.functions.put(methodName, function);
            filteredFunctions.put(methodName, function);
        });
        return filteredFunctions;
    }

    public String getDataset() {
        return dataset;
    }

    public String getSourcePath() {
        return sourcePath;
    }

    public String getClassName() {
        return className;
    }

    public String getPackageName() {
        return packageName;
    }
}
