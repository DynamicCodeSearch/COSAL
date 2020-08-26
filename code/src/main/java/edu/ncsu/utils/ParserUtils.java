package edu.ncsu.utils;

import com.github.javaparser.ParseResult;
import com.github.javaparser.ast.CompilationUnit;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.io.File;

public class ParserUtils {

    private String sourcePath;

    ParseResult<CompilationUnit> parseResult;

    public ParserUtils(String sourcePath) {
        this.sourcePath = sourcePath;
        parseResult = VisitorHelper.parseFile(sourcePath);
    }

    public String getPackage() {
        CompilationUnit compilationUnit = VisitorHelper.loadCompilationUnit(parseResult);
        return VisitorHelper.getPackage(compilationUnit);
    }

    public static String getClassName(String sourcePath) {
        int start = sourcePath.lastIndexOf(File.separator) + 1;
        int end = sourcePath.lastIndexOf(".");
        return sourcePath.substring(start, end);
    }

    public String makeKey() {
        return String.format("%s.%s", getPackage(), getClassName(sourcePath));
    }

    public static void main(String[] args) {
        ParserUtils parserUtils = new ParserUtils("/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/guava/src/com/google/common/base/permutated_class_11e3fe5a1c3146c1a3c645fbe76825fa.java");
        String classKey = parserUtils.makeKey();
        System.out.println(PackageManager.findGeneratedClass(classKey));
    }

}
