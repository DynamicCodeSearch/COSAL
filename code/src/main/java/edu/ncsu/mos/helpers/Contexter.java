package edu.ncsu.mos.helpers;

import edu.ncsu.config.hyperparameters.HyperParameters;
import edu.ncsu.visitors.parsers.ParserUtils;
import org.apache.commons.lang3.StringUtils;

import java.io.IOException;
import java.io.StreamTokenizer;
import java.io.StringReader;
import java.util.HashSet;
import java.util.Set;
import java.util.logging.Logger;

public class Contexter {

    private final static Logger LOGGER = Logger.getLogger(Contexter.class.getName());

    private static StreamTokenizer initializeTokenizer(String sourceCode) {
        StreamTokenizer tokenizer = new StreamTokenizer(new StringReader(sourceCode));
        tokenizer.parseNumbers();
        tokenizer.wordChars('_', '_');
        tokenizer.eolIsSignificant(true);
//        tokenizer.ordinaryChars(0, ' ');
        tokenizer.ordinaryChar('.');
        tokenizer.slashSlashComments(true);
        tokenizer.slashStarComments(true);
        return tokenizer;
    }

    private static String removeNonLetters(String str) {
        return str.replaceAll("[^a-zA-Z]+", "");
    }

    private static String[] splitOnNonLetters(String str) {
        return str.split("[^a-zA-Z]+");
    }

    private static String[] camelCaseSplit(String str) {
        return StringUtils.splitByCharacterTypeCamelCase(str);
    }

    private static boolean isLegitWord(String str) {
        String strLower = str.toLowerCase();
        return str.length() >= HyperParameters.MIN_CONTEXT_TOKEN_SIZE
                && !ParserUtils.isJavaKeyword(str)
                && !ParserUtils.isStopword(strLower);
    }

    private static Set<String> getStringTokens(String str) {
        Set<String> tokens = new HashSet<>();
        if (!isLegitWord(str))
            return tokens;
        String[] splits = str.split("\\s+");
        for (String split: splits) {
            if (isLegitWord(split))
                tokens.add(split.toLowerCase());
            String[] letterSplits = splitOnNonLetters(split);
            for (String letterSplit: letterSplits) {
                if (isLegitWord(letterSplit))
                    tokens.add(letterSplit.toLowerCase());
                String[] camelCaseSplits = camelCaseSplit(letterSplit);
                for (String s: camelCaseSplits) {
                    if (isLegitWord(s))
                        tokens.add(s.toLowerCase());
                }
            }
        }
        return tokens;
    }

    public static Set<String> tokenize(String functionBody) {
        Set<String> tokens = new HashSet<>();
        try {
            StreamTokenizer tokenizer = initializeTokenizer(functionBody);
            int token = tokenizer.nextToken();
            while (token != StreamTokenizer.TT_EOF) {
                switch (token) {
                    case '\"':
                    case StreamTokenizer.TT_WORD:
                        tokens.addAll(getStringTokens(tokenizer.sval));
                        break;
                    default:
                }
                token = tokenizer.nextToken();
            }
        } catch (IOException e) {
            LOGGER.severe(String.format("@COSAL: Error in tokenizing. '%s'", e.getMessage()));
            throw new RuntimeException(e);
        }
        return tokens;
    }

}
