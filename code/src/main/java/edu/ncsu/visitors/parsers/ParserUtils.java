package edu.ncsu.visitors.parsers;

import edu.ncsu.config.ProjectConfig;
import edu.ncsu.utils.Utils;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class ParserUtils {

    private final static Set<String> _KEYWORDS = new HashSet<>();

    private final static Set<Character> _OPERATORS = new HashSet<>();

    private final static Set<String> _STOPWORDS = new HashSet<>();

    public static Set<Character> getOperatorSymbols() {
        if (_OPERATORS.size() != 0)
            return _OPERATORS;
        Character[] ops = {
                '+', '-', '*', '/', '%',
                '=',
                '|', '&', '^',
                '!', '<', '>'
        };
        Collections.addAll(_OPERATORS, ops);
        return _OPERATORS;
    }

    public static Set<String> getJavaKeywords() {
        if (_KEYWORDS.size() != 0)
            return _KEYWORDS;
        String [] kws = {
                "abstract", "continue",     "for",          "new",          "switch",
                "assert",   "default",      "if",           "package",      "synchronized",
                "boolean",  "do",           "goto",         "private",      "this",
                "break",    "double",       "implements",   "protected",    "throw",
                "byte",     "else",         "import",       "public",       "throws",
                "case",     "enum",         "instanceof",   "return",       "transient",
                "catch",    "extends",      "int",          "short",        "try",
                "char",     "final",        "interface",    "static",       "void",
                "class",    "finally",      "long",         "strictfp",     "volatile",
                "const",    "float",        "native",       "super",        "while",
                "null",     "true",         "false"
        };
        Collections.addAll(_KEYWORDS, kws);
        return _KEYWORDS;
    }

    public static boolean isJavaKeyword(String word) {
        return getJavaKeywords().contains(word);
    }

    public static Set<String> getStopwords() {
        if (_STOPWORDS.size() != 0)
            return _STOPWORDS;
        String stopwords_path = Utils.pathJoin(ProjectConfig.CODESEER_HOME, "code", "src", "main", "resources", "stopwords_english.txt");
        try {
            List<String> lines = Files.readAllLines(Paths.get(stopwords_path));
            for (String line: lines)
                _STOPWORDS.add(line.trim());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return _STOPWORDS;
    }

    public static boolean isStopword(String word) {
        return getStopwords().contains(word);
    }

}
