package edu.ncsu.utils;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.*;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IJDKStore;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.io.File;
import java.io.IOException;
import java.lang.reflect.Constructor;
import java.lang.reflect.Executable;
import java.lang.reflect.Method;
import java.util.*;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;
import java.util.logging.Logger;
import java.util.regex.Pattern;

public class JDKUtils {

    private final static Logger LOGGER = Logger.getLogger(JDKUtils.class.getName());

    private final static String JDK_SOURCE_CODE_PATH = Utils.pathJoin(Settings.JDK_SOURCE_PATH, "src");

    private final static IJDKStore JDK_STORE = BaseStorage.loadJDKStore(ProjectConfig.DATASET);

    private final static Pattern CLASS_NAME_PATTERN = Pattern.compile("[a-zA-Z_$][a-zA-Z\\d_$]*");

    private static Set<String> JDK_CLASSES = null;

    @SuppressWarnings("rawtypes")
    public static String makeKey(Executable methodOrConstructor) {
        String classKey = methodOrConstructor.getDeclaringClass().getName();
        String methodName = methodOrConstructor.getName();
        List<String> paramTypes = new ArrayList<>();
        for (Class paramType : methodOrConstructor.getParameterTypes()) {
            paramTypes.add(paramType.getSimpleName());
        }
        String paramString = paramTypes.size() > 0 ? String.join(",", paramTypes) : "";
        return String.format("%s$%s(%s)", classKey, methodName, paramString);
    }

    private static boolean isValidClassName(String className) {
        return CLASS_NAME_PATTERN.matcher(className).matches();
    }

    @SuppressWarnings("rawtypes")
    public static Set<String> getJdkClasses() {
        if (JDK_CLASSES != null)
            return JDK_CLASSES;
        JDK_CLASSES = new HashSet<>();
        try {
            JarFile jarFile = new JarFile(Settings.JDK_JAR_PATH);
            Enumeration<JarEntry> e = jarFile.entries();
            while (e.hasMoreElements()) {
                JarEntry je = e.nextElement();
                if (je.isDirectory() || !je.getName().endsWith(".class"))
                    continue;
                String className = je.getName().substring(0,je.getName().length()-6).replace(File.separatorChar, '.');
                if (!className.startsWith("java."))
                    continue;
                Class clazz = Class.forName(className);
                JDK_CLASSES.add(clazz.getSimpleName());
            }
        } catch (IOException | ClassNotFoundException e) {
            LOGGER.severe("**Note from COSAL**: Check the jar to check if it has .class files and not .java files. If not you might want to add the jar without the sources.");
            throw new RuntimeException(e);
        }
        return JDK_CLASSES;
    }

    private static String makeKey(String classKey, ConstructorDeclaration constructor) {
        List<String> paramTypes = new ArrayList<>();
        for (Parameter parameter : constructor.getParameters()) {
            paramTypes.add(parameter.getTypeAsString());
        }
        String paramString = paramTypes.size() > 0 ? String.join(",", paramTypes) : "";
        return String.format("%s$%s(%s)", classKey, classKey, paramString);
    }

    private static String makeKey(String classKey, MethodDeclaration method) {
        List<String> paramTypes = new ArrayList<>();
        String methodName = method.getNameAsString();
        for (Parameter parameter : method.getParameters()) {
            paramTypes.add(parameter.getTypeAsString());
        }
        String paramString = paramTypes.size() > 0 ? String.join(",", paramTypes) : "";
        return String.format("%s$%s(%s)", classKey, methodName, paramString);
    }


    @SuppressWarnings("rawtypes")
    private static CallableDeclaration getMethodAST(Executable methodOrConstructor) {
        String key = makeKey(methodOrConstructor);
        Class clazz = methodOrConstructor.getDeclaringClass();
        String classKey = clazz.getName();
        String sourcePath = Utils.pathJoin(JDK_SOURCE_CODE_PATH, String.format("%s.java", classKey.replace(".", File.separator)));
        CompilationUnit compilationUnit = VisitorHelper.loadCompilationUnit(VisitorHelper.parseFile(sourcePath));
        boolean isConstructor = methodOrConstructor instanceof Constructor;
        boolean isMethod = methodOrConstructor instanceof Method;
        for (TypeDeclaration typeDeclaration : compilationUnit.getTypes()) {
            if (!typeDeclaration.getName().getIdentifier().equals(clazz.getSimpleName()))
                continue;
            for (Object methodDeclaration : typeDeclaration.getMembers()) {
                if (methodDeclaration instanceof ConstructorDeclaration && isConstructor) {
                    String constructorKey = makeKey(classKey, (ConstructorDeclaration) methodDeclaration);
                    if (constructorKey.equals(key))
                        return (ConstructorDeclaration) methodDeclaration;
                } else if (methodDeclaration instanceof MethodDeclaration && isMethod) {
                    String methodKey = makeKey(classKey, (MethodDeclaration) methodDeclaration);
                    if (methodKey.equals(key))
                        return (MethodDeclaration) methodDeclaration;
                }
            }
        }
        return null;
    }

    @SuppressWarnings("rawtypes")
    public static List<String> getParameterNames(CallableDeclaration methodOrConstructor) {
        List<String> paramNames = new ArrayList<>();
        for (Object parameter : methodOrConstructor.getParameters()) {
            paramNames.add(((Parameter) parameter).getNameAsString());
        }
        return paramNames;
    }


    @SuppressWarnings("rawtypes")
    public static String[] getParameterNames(Executable methodOrConstructor) {
        String key = makeKey(methodOrConstructor);
        JsonObject methodOrConstructorData = JDK_STORE.loadMethod(key);
        if (methodOrConstructorData != null) {
            if (methodOrConstructorData.has("paramNames")) {
                JsonArray paramNamesJSON = methodOrConstructorData.get("paramNames").getAsJsonArray();
                List<String> paramNames = new ArrayList<>();
                for (JsonElement element : paramNamesJSON) {
                    paramNames.add(element.getAsString());
                }
                return Arrays.asList(paramNames.toArray()).toArray(new String[0]);
            }
            return null;
        } else {
            CallableDeclaration ast = getMethodAST(methodOrConstructor);
            JsonObject methodParamNames = new JsonObject();
            methodParamNames.addProperty("key", key);
            boolean isValid = false;
            List<String> paramNames = null;
            if (ast != null) {
                isValid = true;
                paramNames = getParameterNames(ast);
                if (paramNames.size() > 0) {
                    JsonArray names = new JsonArray();
                    for (String paramName : paramNames)
                        names.add(paramName);
                    methodParamNames.add("paramNames", names);
                }
            }
            methodParamNames.addProperty("isValid", isValid);
            JDK_STORE.saveMethod(methodParamNames);
            if (!isValid)
                throw new RuntimeException(String.format("@COSAL: Method: '%s' is not valid.", key));
            if (paramNames.size() > 0){
                return Arrays.asList(paramNames.toArray()).toArray(new String[0]);
            }
            return null;
        }
    }

    public static void main(String[] args) throws Exception {
        System.out.println(getJdkClasses());
//        Class clazz = PackageManager.findGeneratedClass("java.lang.StringBuilder");
//        Constructor constructor = clazz.getDeclaredConstructor(String.class);
//        System.out.println(Arrays.toString(getParameterNames(constructor)));
//        System.out.println(makeKey(constructor));
//        Method method = clazz.getMethod("append", String.class);
//        System.out.println(makeKey(method));
    }

}
