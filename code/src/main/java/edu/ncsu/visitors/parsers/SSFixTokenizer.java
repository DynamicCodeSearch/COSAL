package edu.ncsu.visitors.parsers;

import com.github.javaparser.ParseResult;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.NodeList;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.Expression;
import com.github.javaparser.ast.expr.FieldAccessExpr;
import com.github.javaparser.ast.expr.MethodCallExpr;
import com.github.javaparser.ast.expr.NameExpr;
import com.github.javaparser.ast.stmt.Statement;
import com.github.javaparser.ast.type.ClassOrInterfaceType;
import com.github.javaparser.ast.type.Type;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import com.google.gson.*;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.hyperparameters.HyperParameters;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.store.ITokenStore;
import edu.ncsu.utils.JDKUtils;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.logging.Logger;


public class SSFixTokenizer {

    private final static Logger LOGGER = Logger.getLogger(SSFixTokenizer.class.getName());

    private final static String TOKEN_LITERAL_STRING = "$ls$";

    private final static String TOKEN_LITERAL_NUMBER = "$ln$";

    private final static String TOKEN_LITERAL_BOOLEAN = "$lb$";

    private final static String TOKEN_NON_JDK_TYPE = "$t";

    private final static String TOKEN_NON_JDK_METHODS_PRE = "__SLACC__m";

    private final static String TOKEN_NON_JDK_FIELDS_PRE = "__SLACC__m";

    private final static String TOKEN_VARIABLE = "$v";

    private final static String TOKEN_NON_JDK_METHODS = "$m";

    private final static String TOKEN_NON_JDK_FIELDS = "$m";

    private List<String> sourceCodeLines;

    private static IMetadataStore _METADATA_STORE = null;

    private static ITokenStore _TOKEN_STORE = null;

    private TokenizerVisitor visitor;

    public TokenizerVisitor getVisitor() {
        return visitor;
    }

    public SSFixTokenizer(String sourceCode) {
        this.visitor = new TokenizerVisitor(sourceCode);
        this.sourceCodeLines = this.visitor.getCodeBodyAsList();
    }

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

    private static String getTokenLiteralString(String word) {
        return word.contains(" ") ? TOKEN_LITERAL_STRING : String.format("\"%s\"", word);
    }


    private boolean isBoolean(String word) {
        return "true".equals(word) || "false".equals(word);
    }

    private boolean isJDKType(String word) {
        return visitor.getJDKTypes().contains(word);
    }

    private boolean isNonJDKType(String word) {
        return visitor.getNonJDKTypes().contains(word);
    }

    private boolean isVariable(String word) {
        return visitor.getJDKVariables().contains(word) || visitor.getNonJDKVariables().contains(word);
    }

    private List<String> getTokens(String word) {
        if (isBoolean(word)) {
            return Collections.singletonList(TOKEN_LITERAL_BOOLEAN);
        } else if (ParserUtils.isJavaKeyword(word)) {
            return Collections.singletonList(word);
        } else if (isJDKType(word)) {
            return Collections.singletonList(word);
        } else if (isNonJDKType(word)) {
            return Collections.singletonList(TOKEN_NON_JDK_TYPE);
        } else if (isVariable(word)) {
            return Collections.singletonList(TOKEN_VARIABLE);
        } else if (word.equals(TOKEN_NON_JDK_METHODS_PRE)) {
            return Collections.singletonList(TOKEN_NON_JDK_METHODS);
        } else if (word.equals(TOKEN_NON_JDK_FIELDS_PRE)) {
            return Collections.singletonList(TOKEN_NON_JDK_FIELDS);
        } else {
            return Collections.singletonList(word);
        }
    }

    private boolean isOperator(int token) {
        return ParserUtils.getOperatorSymbols().contains((char) token);
    }

    private List<List<String>> generateTokens() {
        List<List<String>> statementsTokens = new ArrayList<>();
        try {
            for (String statement: sourceCodeLines) {
                List<String> tokens = new ArrayList<>();
                StreamTokenizer codeTokenizer = initializeTokenizer(statement);
                int token = codeTokenizer.nextToken();
                while (token != StreamTokenizer.TT_EOF) {
                    switch (token) {
                        case StreamTokenizer.TT_NUMBER:
                            tokens.add(TOKEN_LITERAL_NUMBER);
                            break;
                        case '"':
                            tokens.add(getTokenLiteralString(codeTokenizer.sval));
                            break;
                        case '\'':
                            tokens.add(String.format("'%s'", codeTokenizer.sval));
                            break;
                        case StreamTokenizer.TT_WORD:
                            List<String> tokenized = getTokens(codeTokenizer.sval);
                            if (tokenized.size() > 0)
                                tokens.addAll(tokenized);
                            break;
                        default:
                            StringBuilder tokenString = new StringBuilder();
                            if (isOperator(token)) {
                                while (isOperator(token)) {
                                    tokenString.append((char) token);
                                    token = codeTokenizer.nextToken();
                                }
                                tokens.add(tokenString.toString());
                                continue;
                            } else {
                                tokenString.append((char) token);
                                if (tokenString.length() > 0)
                                    tokens.add(tokenString.toString());
                            }
                    }
//                System.out.println(String.format("Token: '%s'; value: '%s", tokenizer.ttype, tokenizer.sval));
                    token = codeTokenizer.nextToken();
                }
                if (tokens.size() > 0)
                    statementsTokens.add(tokens);
            }
        } catch (IOException e) {
            LOGGER.severe(String.format("@COSAL: Error in tokenizing. '%s'", e.getMessage()));
            throw new RuntimeException(e);
        }
        return statementsTokens;
    }

    public List<List<String>> tokenize(int tokenSize) {
        List<List<String>> tokenGroups = new ArrayList<>();
        List<List<String>> generatedTokens = generateTokens();
        for (List<String> stmtTokens: generatedTokens) {
            if (stmtTokens.size() < tokenSize) {
                tokenGroups.add(stmtTokens);
            } else {
                for (int i=0; i < stmtTokens.size() - tokenSize; i++) {
                    tokenGroups.add(stmtTokens.subList(i, i + tokenSize));
                }
            }
        }
        return tokenGroups;
    }

    public static List<List<String>> tokenize(String functionBody, int tokenSize) {
        String tokenClassBody = String.format("public class SampleTokenClass {\n %s \n}", functionBody);
        SSFixTokenizer tokenizer = new SSFixTokenizer(tokenClassBody);
        return tokenizer.tokenize(tokenSize);
    }

    public static long getHashKey(List<List<String>> tokens) {
        List<String> joined = new ArrayList<>();
        for (List<String> tokenGroup: tokens)
            joined.add(String.join("@@", tokenGroup));
        return String.join("$$", joined).hashCode();
    }

    public static void tokenizeDataset() {
        int tokenSize = HyperParameters.TOKEN_SIZE;
        LOGGER.info("Fetching functions .... ");
        Map<String, JsonObject> generatedFunctionBodies = SSFixTokenizer.loadMetadataStore().loadGeneratedFunctionBodies();
        int index = 0;
        for (String name: generatedFunctionBodies.keySet()) {
            if (index % 100 == 0)
                LOGGER.info(String.format("Tokenizing function: %d / %d ... ", index + 1, generatedFunctionBodies.size()));
            JsonObject generatedFunction = generatedFunctionBodies.get(name);
            String functionBody = generatedFunction.get("body").getAsString();
            List<List<String>> tokens = tokenize(functionBody, tokenSize);
            JsonObject functionTokenObj = new JsonObject();
            long hashCode = getHashKey(tokens);
            functionTokenObj.addProperty("name", name);
            functionTokenObj.addProperty("body", functionBody);
            functionTokenObj.addProperty("hash_key", hashCode);
            functionTokenObj.add("tokens", new Gson().toJsonTree(tokens).getAsJsonArray());
            SSFixTokenizer.loadTokenStore().saveTokens(functionTokenObj);
            index++;
        }
    }


    @SuppressWarnings("rawtypes")
    static class TokenizerVisitor extends VoidVisitorAdapter {

        private ParseResult<CompilationUnit> compilationUnitParseResult;

        private Set<String> jDKTypes = new HashSet<>();

        private Set<String> nonJDKTypes = new HashSet<>();

        private Set<String> jDKVariables = new HashSet<>();

        private Set<String> nonJDKVariables = new HashSet<>();

        public Set<String> getJDKTypes() {
            return jDKTypes;
        }

        public Set<String> getNonJDKTypes() {
            return nonJDKTypes;
        }

        public Set<String> getJDKVariables() {
            return jDKVariables;
        }

        public Set<String> getNonJDKVariables() {
            return nonJDKVariables;
        }

        private boolean isJDKClass(String className) {
            return JDKUtils.getJdkClasses().contains(className);
        }

        @SuppressWarnings("unchecked")
        public TokenizerVisitor(String sourceCode) {
            this.compilationUnitParseResult = VisitorHelper.parseSourceCode(sourceCode);
            CompilationUnit compilationUnit = VisitorHelper.loadCompilationUnit(this.compilationUnitParseResult);
            this.visit(compilationUnit, null);
        }

        public String getCodeBody() {
            List<String> statements = getCodeBodyAsList();
            if (statements == null)
                return null;
            return String.join("\n", statements);
        }

        private List<String> getCodeBodyAsList() {
            CompilationUnit compilationUnit = VisitorHelper.loadCompilationUnit(this.compilationUnitParseResult);
            for (TypeDeclaration typeDeclaration: compilationUnit.getTypes()) {
                if (!(typeDeclaration instanceof ClassOrInterfaceDeclaration))
                    continue;
                for (Object met: typeDeclaration.getMethods()) {
                    MethodDeclaration method = (MethodDeclaration) met;
                    if (!method.getBody().isPresent())
                        continue;
                    NodeList<Statement> stmts = method.getBody().get().getStatements();
                    List<String> statementStrings = new ArrayList<>();
                    for (Statement stmt: stmts) {
                        statementStrings.add(stmt.toString());
                    }
                    return statementStrings;
                }
            }
            return null;
        }

        private boolean updateNonJDKTypes(Type classType) {
            if (!(classType.getElementType() instanceof ClassOrInterfaceType))
                return false;
            ClassOrInterfaceType classParamType = (ClassOrInterfaceType) classType.getElementType();
            String classString = classParamType.getNameAsString();
            boolean isJDKClass = isJDKClass(classString);
            if (isJDKClass) {
                jDKTypes.add(classString);
            } else {
                nonJDKTypes.add(classString);
            }

            if (classParamType.getTypeArguments().isPresent()) {
                for (Type typeArgument: classParamType.getTypeArguments().get())
                    updateNonJDKTypes(typeArgument);
            }
            return !isJDKClass;
        }



        private boolean isScopeFromJDK(Expression expression) {
            if (expression instanceof MethodCallExpr) {
                MethodCallExpr expr = (MethodCallExpr) expression;
                if (expr.getScope().isPresent()) {
                    return isScopeFromJDK(expr.getScope().get());
                }
                return false;
            } else if (expression instanceof FieldAccessExpr) {
                FieldAccessExpr expr = (FieldAccessExpr) expression;
                return isScopeFromJDK(expr.getScope());
            } else if (expression instanceof NameExpr) {
                NameExpr expr = (NameExpr) expression;
                return jDKVariables.contains(expr.getNameAsString()) || isJDKClass(expr.getNameAsString());
            } else {
                return false;
            }
        }

        @Override
        @SuppressWarnings("unchecked")
        public void visit(MethodDeclaration n, Object arg) {
            n.getName().accept(this, arg);
            n.getParameters().forEach(p -> p.accept(this, arg));
            n.getReceiverParameter().ifPresent(l -> l.accept(this, arg));
            n.getType().accept(this, arg);
            n.getModifiers().forEach(p -> p.accept(this, arg));
            n.getThrownExceptions().forEach(p -> p.accept(this, arg));
            n.getBody().ifPresent(l -> l.accept(this, arg));
            n.getTypeParameters().forEach(p -> p.accept(this, arg));
            n.getAnnotations().forEach(p -> p.accept(this, arg));
            n.getComment().ifPresent(l -> l.accept(this, arg));
        }

        @SuppressWarnings("unchecked")
        public void visit(VariableDeclarator variable, Object arg) {
            Type variableType = variable.getType();
            String variableName = variable.getNameAsString();
            boolean isNonJDKClass = updateNonJDKTypes(variableType);
            if (isNonJDKClass) {
                nonJDKVariables.add(variableName);
            } else {
                jDKVariables.add(variableName);
            }
            variable.getInitializer().ifPresent(l -> l.accept(this, arg));
            variable.getName().accept(this, arg);
            variable.getType().accept(this, arg);
            variable.getComment().ifPresent(l -> l.accept(this, arg));
//            variable.setName(TOKEN_VARIABLE);
        }

        @SuppressWarnings("unchecked")
        public void visit(Parameter parameter, Object arg) {
            Type paramType = parameter.getType();
            boolean isNonJDKClass = updateNonJDKTypes(paramType);
            String paramName = parameter.getNameAsString();
            if (isNonJDKClass) {
                nonJDKVariables.add(paramName);
            } else {
                jDKVariables.add(paramName);
            }
            parameter.getAnnotations().forEach(p -> p.accept(this, arg));
            parameter.getModifiers().forEach(p -> p.accept(this, arg));
            parameter.getName().accept(this, arg);
            parameter.getVarArgsAnnotations().forEach(p -> p.accept(this, arg));
            parameter.getComment().ifPresent(l -> l.accept(this, arg));
        }

        @SuppressWarnings("unchecked")
        public void visit(MethodCallExpr expr, Object arg) {
            boolean isScopeFromJDK = false;
            if (expr.getScope().isPresent()) {
                isScopeFromJDK = isScopeFromJDK(expr.getScope().get());
            }
            expr.getArguments().forEach(p -> p.accept(this, arg));
            expr.getName().accept(this, arg);
            expr.getScope().ifPresent(l -> l.accept(this, arg));
            expr.getTypeArguments().ifPresent(l -> l.forEach(v -> v.accept(this, arg)));
            expr.getComment().ifPresent(l -> l.accept(this, arg));
            if (!isScopeFromJDK) {
                expr.setName(TOKEN_NON_JDK_METHODS_PRE);
            }
        }

        @SuppressWarnings("unchecked")
        public void visit(FieldAccessExpr expr, Object arg) {
            boolean isScopeFromJDK = isScopeFromJDK(expr.getScope());
            expr.getName().accept(this, arg);
            expr.getScope().accept(this, arg);
            expr.getTypeArguments().ifPresent(l -> l.forEach(v -> v.accept(this, arg)));
            expr.getComment().ifPresent(l -> l.accept(this, arg));
            if (!isScopeFromJDK) {
                expr.setName(TOKEN_NON_JDK_FIELDS_PRE);
            }
        }

    }

    public static void test() {
        String data;
        SSFixTokenizer tokenizer;
        try {
            data = new String(Files.readAllBytes(Paths.get("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/_rough/sample_java_code2.txt")));
            tokenizer = new SSFixTokenizer(data);
            System.out.println("\nCode Body:");
            System.out.println(tokenizer.getVisitor().getCodeBody());
            System.out.println("\nTokens:");
            List<List<String>> statementTokens = tokenizer.tokenize(3);
            System.out.println(statementTokens);
        } catch (IOException e){
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        tokenizeDataset();
//        test();
    }

}


