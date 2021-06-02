package edu.ncsu.executors.helpers;

import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.utils.Utils;

import java.io.File;
import java.io.IOException;
import java.net.*;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;
import java.util.logging.Logger;

public class PackageManager {

    private static final Logger LOGGER = Logger.getLogger(PackageManager.class.getName());

    private static ClassLoader CLASS_LOADER = (URLClassLoader)ClassLoader.getSystemClassLoader();

    static {
        if (ProjectConfig.JAR_NAME != null) {
            CLASS_LOADER = new URLClassLoader(new URL[] {Utils.getJarURL(Settings.PROJECTS_JAR_PATH)}, ClassLoader.getSystemClassLoader());
        }
    }

    @SuppressWarnings("rawtypes")
    public static List<Class> findClasses(String packageName) {
        try {
            List<Class> classes = new ArrayList<>();
            ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
            assert classLoader != null;
            String path = packageName.replace('.', '/');
            Enumeration<URL> resources = classLoader.getResources(path);
            List<File> dirs = new ArrayList<>();
            while (resources.hasMoreElements()) {
                URL resource = resources.nextElement();
                dirs.add(new File(resource.getFile()));
            }
            for (File directory : dirs) {
                classes.addAll(findClasses(directory, packageName));
            }
            return classes;
        } catch (IOException | ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    @SuppressWarnings("rawtypes")
    private static List<Class> findClasses(File directory, String packageName) throws ClassNotFoundException {
        List<Class> classes = new ArrayList<>();
        if (!directory.exists()) {
            return classes;
        }
        File[] files = directory.listFiles();
        for (File file : files) {
            if (file.isDirectory()) {
                assert !file.getName().contains(".");
                classes.addAll(findClasses(file, packageName + "." + file.getName()));
            } else if (file.getName().endsWith(".class")) {
                classes.add(Class.forName(packageName + '.' + file.getName().substring(0, file.getName().length() - 6)));
            }
        }
        return classes;
    }

    @SuppressWarnings("rawtypes")
    public static Class findClass(String classKey) {
        try {
            return CLASS_LOADER.loadClass(classKey);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    public static ArrayList<String> getClassNamesFromPackage(String packageName) {
        URL packageURL;
        ArrayList<String> names = new ArrayList<String>();;

        packageName = packageName.replace(".", "/");
        packageURL = CLASS_LOADER.getResource(packageName);

        try {
            if (packageURL.getProtocol().equals("jar")) {
                String jarFileName;
                JarFile jf ;
                Enumeration<JarEntry> jarEntries;
                String entryName;
                // build jar file name, then loop through zipped entries
                jarFileName = URLDecoder.decode(packageURL.getFile(), "UTF-8");
                jarFileName = jarFileName.substring(5,jarFileName.indexOf("!"));
                jf = new JarFile(jarFileName);
                jarEntries = jf.entries();
                while(jarEntries.hasMoreElements()){
                    entryName = jarEntries.nextElement().getName();
                    if(entryName.startsWith(packageName) && entryName.length()>packageName.length()+5){
                        entryName = entryName.substring(0, entryName.length()-6).replace(File.separator.charAt(0), '.');
//                        entryName = entryName.substring(packageName.length(),entryName.lastIndexOf('.'));
                        names.add(entryName);
                    }
                }
                // loop through files in classpath
            } else {
                URI uri = new URI(packageURL.toString());
                File folder = new File(uri.getPath());
                // won't work with path which contains blank (%20)
                // File folder = new File(packageURL.getFile());
                File[] contenuti = folder.listFiles();
                String entryName;
                for(File actual: contenuti){
                    entryName = actual.getName();
                    entryName = packageName + entryName.substring(0, entryName.lastIndexOf('.'));
                    names.add(entryName);
                }
            }
        } catch (IOException | URISyntaxException e) {
            throw new RuntimeException(e);
        }
        return names;
    }

    public static List<Class> getClassesFromPackage(String packageName) {
        List<String> classNames = getClassNamesFromPackage(packageName);
        List<Class> classes = new ArrayList<>();
        for (String className: classNames) {
            try {
                classes.add(CLASS_LOADER.loadClass(className));
            } catch (ClassNotFoundException e) {
                LOGGER.severe(String.format("Class '%s' not found", className));
                e.printStackTrace();
            }
        }
        return classes;

    }


    @SuppressWarnings("rawtypes")
    private static Class loadClassFromJar(String classKey, String jarPath) {
        try {
            JarFile jarFile = new JarFile(jarPath);
            Enumeration<JarEntry> e = jarFile.entries();
            while (e.hasMoreElements()) {
                JarEntry je = e.nextElement();
                if(je.isDirectory() || !je.getName().endsWith(".class")){
                    continue;
                }
                String clazzName = je.getName().substring(0,je.getName().length()-6).replace(File.separator.charAt(0), '.');
                // -6 because of .class
                if (classKey.equals(clazzName)) {
                    return CLASS_LOADER.loadClass(clazzName);
                }
            }
        } catch (IOException | ClassNotFoundException e) {
//            LOGGER.severe(ExceptionUtils.getStackTrace(e));
            LOGGER.severe("**Note from COSAL**: Check the jar to check if it has .class files and not .java files. If not you might want to add the jar without the sources.");
            throw new RuntimeException(e);
        }
        return null;
    }

    @SuppressWarnings("rawtypes")
    public static Class loadClassFromSourceJar(String classKey) {
        return loadClassFromJar(classKey, Settings.PROJECTS_JAR_PATH);
    }

    @SuppressWarnings("rawtypes")
    public static Class loadClassFromJDK(String classKey) {
        return loadClassFromJar(classKey, Settings.JDK_JAR_PATH);
    }

    @SuppressWarnings("rawtypes")
    public static boolean isClassFromJDK(Class clazz) {
        return loadClassFromJar(ReflectionHelper.makeKey(clazz), Settings.JDK_JAR_PATH) != null;
    }

    @SuppressWarnings("rawtypes")
    public static Class findGeneratedClass(String classKey) {
        Class clazz = loadClassFromSourceJar(classKey);
        if (clazz == null)
            clazz = loadClassFromJDK(classKey);
        return clazz;
    }

    public static void main(String[] args) throws RuntimeException{
        for (Class clazz: getClassesFromPackage("C73.P0.S1577233"))
            System.out.println(clazz);
    }



}
