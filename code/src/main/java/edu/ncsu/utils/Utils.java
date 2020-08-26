package edu.ncsu.utils;

import com.google.gson.JsonObject;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import org.apache.commons.io.FileUtils;
import org.apache.commons.io.IOUtils;
import org.apache.commons.lang3.StringUtils;

import java.io.*;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.logging.Logger;

public class Utils {

    private static Logger LOGGER = Logger.getLogger(Utils.class.getName());

    /**
     * Create a directory if it does not exist
     * @param dirName - Path of the directory
     */
    public static void mkdir(String dirName) {
        File dir = new File(dirName);
        if (!dir.exists()) {
            dir.mkdirs();
        }
    }

    /***
     * List directories in folder
     * @param dirName Name of directory
     * @return List of subdirectories
     */
    public static String[] listDir(String dirName) {
        File dir = new File(dirName);
        String[] directories = dir.list((dir1, name) -> new File(dir1, name).isDirectory());
        return directories;
    }

    /***
     * Delete folder
     * @param path - Path for file/folder to delete
     */
    public static void deleteFileOrFolder(String path) {
        File f = new File(path);
        if (f.exists()) {
            try {
                FileUtils.forceDelete(f);
            } catch (IOException ignored) {}
        }
    }

    /***
     * Delete paths
     * @param paths - List of all paths to delete
     */
    public static void deleteFilesOrFolders(List<String> paths) {
        if (paths == null)
            return;
        for (String path: paths)
            deleteFileOrFolder(path);
    }

    /**
     * Check if the file exists.
     * @param fileName Name of the file
     * @return True if file exists else False.
     */
    public static boolean fileExists(String fileName) {
        File file = new File(fileName);
        return file.exists();
    }

    /**
     * Get name of the file
     * @param path - Path fo the file
     * @return - Name of the file
     */
    public static String getFileName(String path) {
        File file = new File(path);
        return file.getName();
    }

    /***
     * Get the path of the parent folder from the file path
     * @param path - Path of the file
     * @return - Path of the parent folder
     */
    public static String getFolderPath(String path) {
        File file = new File(path);
        return file.getParentFile().getPath();
    }

    /***
     * Return contents of the file.
     * @param path - Path of the file.
     * @return - Contents of the file.
     */
    public static String getFileContent(String path) {
        try {
            return new String(Files.readAllBytes(Paths.get(path)));
        } catch (IOException e) {
            LOGGER.severe("Error while fetching file content: " + e.getMessage());
            return null;
        }
    }

    /**
     * Write contents to file
     * @param content - Contents to be written
     * @param path - Path fo the file
     */
    public static void writeFileContent(String content, String path) {
        try {
            File file = new File(path);
            mkdir(getFolderPath(path));
            FileOutputStream fos = new FileOutputStream(file);
            fos.write(IOUtils.toByteArray(content));
            fos.flush();
            fos.close();
        } catch (IOException e) {
            LOGGER.severe(String.format("Error while writing content to file: %s", path));
            e.printStackTrace();
        }
    }

    /***
     *
     * @param folderPath - Path of the folder to list files
     * @param filter - Instance of java.io.FilenameFilter used to filter the file names
     * @param isAbsolute - If true returns as absolute path
     * @param checkNest - If true nests the folders
     * @return - List of names(absolute/relative) for the files in folder
     */
    public static List<String> listFiles(String folderPath, FilenameFilter filter, boolean isAbsolute, boolean checkNest) {
        File directory = new File(folderPath);
        List<String> files = new ArrayList<>();
        File[] contents = directory.listFiles();
        if (contents == null)
            return files;
        for (File file: contents) {
            if (file.isFile() && filter.accept(directory, file.getAbsolutePath())) {
                if (isAbsolute)
                    files.add(file.getAbsolutePath());
                else
                    files.add(file.getName());
            } else if (checkNest && file.isDirectory()) {
                files.addAll(listFiles(file.getAbsolutePath(), filter, isAbsolute, true));
            }
        }
        return files;
    }

    /**
     * List all files in folder with the matching extension.
     * @param folderPath Path of the folder
     * @param extension Extension to match
     * @param isAbsolute If true, returns absolute path else relative path.
     * @param checkNest If true, checks nested directories as well
     * @param prefixes List of prefixes. If null, returns all files
     * @return - File names/paths as a List of Strings
     */
    public static List<String> listFilesWithExtension(String folderPath, final String extension,
                                                      boolean isAbsolute, boolean checkNest, List<String> prefixes) {
        File directory = new File(folderPath);
        List<String> files = new ArrayList<>();
        File[] contents = directory.listFiles();
        if (contents == null)
            return files;
        for (File file : contents) {
            String fileName = file.getName();
            if (file.isFile() && fileName.endsWith(extension)
                    && (prefixes == null || (prefixes != null && prefixes.stream().anyMatch(fileName::startsWith)))) {
                if (isAbsolute)
                    files.add(file.getAbsolutePath());
                else
                    files.add(file.getName());
            } else if (checkNest && file.isDirectory()) {
                files.addAll(listFilesWithExtension(file.getAbsolutePath(), extension, isAbsolute, true, prefixes));
            }
        }
        return files;
    }

    /**
     * List temporary files in folder
     * @param folderPath - Path of the folder
     * @return - List of paths of temporary files.
     */
    public static List<String> listTemporaryFiles(String folderPath) {
        return listFilesWithExtension(folderPath, ".java", true, true, Collections.singletonList(Settings.TEMPORARY_CLASS_PREFIX));
    }

    /**
     * List permutated files in folder
     * @param folderPath - Path of the folder
     * @return - List of paths of permutated files.
     */
    public static List<String> listPermutatedFiles(String folderPath) {
        return listFilesWithExtension(folderPath, ".java", true, true, Collections.singletonList(Settings.PERMUTATED_CLASS_PREFIX));
    }

    /**
     * List generated files in folder
     * @param folderPath - Path of the folder
     * @return - List of paths of generated files.
     */
    public static List<String> listGeneratedFiles(String folderPath) {
        return listFilesWithExtension(folderPath, ".java", true, true, Collections.singletonList(Settings.GENERATED_CLASS_PREFIX));
    }

    /**
     * List non generated files in folder
     * @param folderPath - Path fo the folder
     * @return - List of paths of non generated files
     */
    public static List<String> listNonGeneratedJavaFiles(String folderPath) {
        File directory = new File(folderPath);
        List<String> files = new ArrayList<>();
        File[] contents = directory.listFiles();
        if (contents == null)
            return files;
        List<String> prefixes = Arrays.asList(Settings.GENERATED_CLASS_PREFIX, Settings.PERMUTATED_CLASS_PREFIX, Settings.TEMPORARY_CLASS_PREFIX);
        for (File file : contents) {
            String fileName = file.getName();
            if (file.isFile() && fileName.endsWith(".java") && prefixes.stream().noneMatch(fileName::startsWith)) {
                files.add(file.getAbsolutePath());
            } else if (file.isDirectory()) {
                files.addAll(listNonGeneratedJavaFiles(file.getAbsolutePath()));
            }
        }
        return files;
    }

    /***
     * Join a list of path by the file separator
     * @param paths - Array of paths to join.
     * @return
     */
    public static String pathJoin(String... paths) {
        return StringUtils.join(paths, File.separator);
    }

    /***
     * Read all lines from a file as a list of strings
     * @param fileName Complete path of the file.
     * @return. Content of file as a list of strings
     */
    public static List<String> readLinesFromFile(String fileName) {
        List<String> lines = new ArrayList<>();
        String line;
        try {
            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            while ((line = reader.readLine()) != null)
                lines.add(line);
            reader.close();
        } catch (IOException ex) {
            System.err.println(ex.getMessage());
            return null;
        }
        return lines;
    }

    /***
     * Read all lines from a file as a string
     * @param fileName Complete path of the file.
     * @return. Content of file as a list of strings
     */
    public static String readFromFile(String fileName) {
        StringBuilder sb = new StringBuilder();
        String line;
        try {
            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            while ((line = reader.readLine()) != null)
                sb.append(line).append("\n");
            reader.close();
        } catch (IOException ex) {
            throw new RuntimeException(ex);
        }
        return sb.toString();
    }

    /***
     * Create a random string.
     * @return Random string
     */
    public static String randomString() {
        return UUID.randomUUID().toString().replaceAll("-", "");
    }

    /***
     * Deep clone of an object
     * @param object
     * @return
     */
    public static Object deepClone(Object object) {
        try {
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(baos);
            oos.writeObject(object);
            ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
            ObjectInputStream ois = new ObjectInputStream(bais);
            return ois.readObject();
        }
        catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    /**
     * Get output stream of string buffer
     * @param process - Instance of Runtime Process
     * @return - Output as string
     */
    public static String getOutput(Process process) {
        try {
            StringBuffer buffer = new StringBuffer();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String s;
            while ((s = reader.readLine()) != null) {
                buffer.append(s).append("\n");
            }
            return buffer.toString();
        } catch (Exception e) {
            return e.getMessage();
        }
    }

    /**
     * Get error stream of string buffer
     * @param process - Instance of Runtime Process
     * @return - Output as string
     */
    public static String getError(Process process) {
        try {
            StringBuffer buffer = new StringBuffer();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getErrorStream()));
            String s;
            while ((s = reader.readLine()) != null) {
                buffer.append(s).append("\n");
            }
            return buffer.toString();
        } catch (Exception e) {
            return e.getMessage();
        }
    }

    /**
     * Get environment variables
     * @return - List of environment variables
     */
    public static String[] getEnvs() {
        List<String> envs = new ArrayList<>();
        Map<String, String> envMap = System.getenv();
        for (String key: envMap.keySet()) {
            envs.add(String.format("%s=%s", key, envMap.get(key)));
        }
        return Arrays.copyOf(envs.toArray(), envs.size(), String[].class);
    }

    /**
     * Get package of class file
     * @param javaFilePath - Path of the java file
     * @return - Package of class
     */
    public static String getPackageName(String javaFilePath) {
        try {
            String packageRelativePath = javaFilePath.split(Settings.SRC_MAIN_JAVA)[1].substring(1);
            int separatorIndex = packageRelativePath.lastIndexOf(File.separator);
            if (separatorIndex == -1) {
                return "default";
            } else {
                return packageRelativePath.substring(0, separatorIndex).replaceAll(File.separator, ".");
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    /**
     * Get name of the class from the path of the file.
     * @param javaFilePath - Path of the file
     * @return - Name of the class
     */
    public static String getClassName(String javaFilePath) {
        String classPath = javaFilePath.split("\\.java")[0].trim();
        int separatorIndex = classPath.lastIndexOf(File.separator);
        return classPath.substring(separatorIndex + 1);
    }

    /***
     * Return the package as the folder in file system
     * @param packageName - Name of the package.
     * @return - Package as folder name
     */
    public static String packageToFolder(String packageName) {
        return packageName.replaceAll("\\.", File.separator);
    }

    /***
     * Convert a hash map to a gson JsonObject
     * @param map - Hash map
     * @return - Hash map as a JsonObject
     */
    public static JsonObject toJson(Map map) {
        JsonObject json = new JsonObject();
        for (Object key: map.keySet()) {
            json.addProperty(key.toString(), map.get(key).toString());
        }
        return json;
    }


    public static URL getJarURL(String pathToJar) {
        try {
            return new URL("jar:file:" + pathToJar + "!/");
        } catch (MalformedURLException e) {
            throw  new RuntimeException(e);
        }
    }

    public static String getRepoLocalPath(String path) {
        int startIndex = path.indexOf(ProjectConfig.ROOT_PATH);
        if (startIndex >= 0)
            return path.substring(startIndex + ProjectConfig.ROOT_PATH.length()+1);
        return path;
    }

    public static String getAbsolutePath(String path) {
        int startIndex = path.indexOf(ProjectConfig.ROOT_PATH);
        if (startIndex >= 0)
            return path;
        return Utils.pathJoin(ProjectConfig.ROOT_PATH, path);
    }

    public static List<?> shuffle(List<?> collection) {
        if (collection == null)
            return null;
        Collections.shuffle(collection);
        return collection;
    }

    public static void main(String[] args) {
//        System.out.println(Utils.getFolderPath("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/Y11R5P1/Joshik/generated_class_d6e333fe2dfc41cfa56782e918726c8b.java"));
//        System.out.println(randomString());
        List<String> prefixes = Arrays.asList(Settings.GENERATED_CLASS_PREFIX,  Settings.PERMUTATED_CLASS_PREFIX);
//        List<String> prefixes = null;
//        System.out.println(listFilesWithExtension2("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Example", ".java", true, true, prefixes));
        System.out.println(getRepoLocalPath("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Dummy"));
    }

}

