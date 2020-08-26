package edu.ncsu.executors.helpers;

import edu.ncsu.config.Settings;
import edu.ncsu.utils.Utils;

import java.io.*;
import java.util.*;

public class FileHandler {

    private final static String RANDOM_OUTPUT_FOLDER = Utils.pathJoin(Settings.CODE_RESOURCES_FOLDER, "test_files_output");

    private final static Set<String> INPUT_CLASSES = new HashSet<>();

    private final static Set<String> OUTPUT_CLASSES = new HashSet<>();

    public final static String FILE_INPUT_TYPE = "__SLACC_FILE_INPUT__";

    public final static String FILE_OUTPUT_TYPE = "__SLACC_FILE_OUTPUT__";

    /***
     * Inputs:
     * java.util.Scanner
     * java.util.BufferedReader
     * java.io.StreamTokenizer
     * java.io.FileReader
     */

    /***
     * Outputs:
     * java.io.PrintWriter
     * java.io.PrintStream
     * java.io.BufferedWriter
     */

    static {
        INPUT_CLASSES.add("java.util.Scanner");
        INPUT_CLASSES.add("java.util.StreamTokenizer");
        INPUT_CLASSES.add("java.io.BufferedReader");
        INPUT_CLASSES.add("java.io.FileReader");

        OUTPUT_CLASSES.add("java.io.PrintWriter");
        OUTPUT_CLASSES.add("java.io.BufferedWriter");
        OUTPUT_CLASSES.add("java.io.FileWriter");
    }


    public static Set<String> getInputClasses() {
        return INPUT_CLASSES;
    }

    public static Set<String> getOutputClasses() {
        return OUTPUT_CLASSES;
    }


    public static boolean isInputType(String fileType) {
        return fileType != null && fileType.equals(FILE_INPUT_TYPE);
    }

    public static boolean isOutputType(String fileType) {
        return fileType != null && fileType.equals(FILE_OUTPUT_TYPE);
    }

    public static boolean isInputClass(String className) {
        return className != null && (INPUT_CLASSES.contains(className) || className.equals(FILE_INPUT_TYPE));
    }

    public static boolean isOutputClass(String className) {
        return className != null && (OUTPUT_CLASSES.contains(className) || className.equals(FILE_OUTPUT_TYPE));
    }

    public static boolean isInputOutputClass(String className) {
        return isInputClass(className) || isOutputClass(className);
    }

    public static boolean isInputOutputType(String type) {
        return FILE_INPUT_TYPE.equals(type) || FILE_OUTPUT_TYPE.equals(type);
    }

    public static boolean isSupportedFileClass(String className) {
        return isInputClass(className) || isOutputClass(className);
    }

    public static Object convertFileInput(String className, String contents) {
        contents = contents.replaceAll("^\"|\"$", "").replace("\\n", System.lineSeparator());
        Reader reader;
        try {
            switch (className) {
                case "java.util.Scanner":
                    return new Scanner(contents);
                case "java.util.StreamTokenizer":
                    reader = new StringReader(contents);
                    return new StreamTokenizer(reader);
                case "java.io.BufferedReader":
                    reader = new StringReader(contents);
                    return new BufferedReader(reader);
                case "java.io.FileReader":
                    File tempFile = new File(writeContentsIntoRandomFile(contents));
                    tempFile.deleteOnExit();
                    return new FileReader(tempFile);
                default:
                    throw new RuntimeException(String.format("WTF!! We do not support %s?", className));
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static String convertFileOutput(Object fileObject, int objUUID, int argIndex) {
        String className = fileObject.getClass().getName();
        try {
            switch (className) {
                case "java.io.PrintWriter":
                    PrintWriter pw = (PrintWriter) fileObject;
                    pw.close();
                    break;
                case "java.io.BufferedWriter":
                    BufferedWriter bw = (BufferedWriter) fileObject;
                    bw.close();
                    break;
                case "java.io.FileWriter":
                    FileWriter fw = (FileWriter) fileObject;
                    fw.close();
                    break;
                default:
                    throw new RuntimeException(String.format("WTF!! We do not support %s?", className));
            }
        } catch (IOException ignored) {}
        return dumpOutputAsText(objUUID, argIndex);
    }

    public static Object convertFileOutput(String className, int objUUID, int argIndex) {
        try {
            File tempFile = new File(getWriteFileName(objUUID, argIndex));
            tempFile.deleteOnExit();
            switch (className) {
                case "java.io.PrintWriter":
                    return new PrintWriter(tempFile);
                case "java.io.BufferedWriter":
                    return new BufferedWriter(new FileWriter(tempFile));
                case "java.io.FileWriter":
                    return new FileWriter(tempFile);
                default:
//                    f.delete();
                    throw new RuntimeException(String.format("WTF!! We do not support %s?", className));
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static String writeContentsIntoRandomFile(String contents) {
        String fileName = getRandomFile();
        File f = new File(fileName);
        try {
            FileWriter fileWriter = new FileWriter(f);
            fileWriter.write(contents);
            fileWriter.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return fileName;
    }

    public static String getRandomFile() {
        Utils.mkdir(RANDOM_OUTPUT_FOLDER);
        return Utils.pathJoin(RANDOM_OUTPUT_FOLDER, String.format("gen_%s.in", Utils.randomString()));
    }

    public static String getWriteFileName(int objUUID, int argIndex) {
        Utils.mkdir(RANDOM_OUTPUT_FOLDER);
        return Utils.pathJoin(RANDOM_OUTPUT_FOLDER, String.format("test-%d-%d.out", objUUID, argIndex));
    }

    public static String dumpOutputAsText(int objUUID, int argIndex) {
        String filePath = getWriteFileName(objUUID, argIndex);
        if (Utils.fileExists(filePath)) {
            return Utils.readFromFile(filePath);
        }
        return null;
    }

    public static void main(String[] args) throws Exception{
        String contents = "Hello Darkness\nMy old friend\nI've come to ..... \n";
        FileReader reader = (FileReader) convertFileInput("java.io.FileReader", contents);
        int i = reader.read();
        while (i != -1) {
            System.out.println(i);
            i = reader.read();
        }

    }

}
