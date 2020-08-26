package edu.ncsu.mos.crawl;

import com.github.javaparser.ParseResult;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.TypeDeclaration;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.mos.blocks.CodeBlock;
import edu.ncsu.mos.helpers.Contexter;
import edu.ncsu.mos.store.CodeStore;
import edu.ncsu.utils.ParserUtils;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.blocks.ImportBlock;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.logging.Logger;


class MethodAdapter extends VoidVisitorAdapter {

    private String filePath;

    private ParseResult<CompilationUnit> compilationUnitParseResult;

    private List<ImportBlock> imports;

    private List<CodeBlock> codeBlocks = new ArrayList<>();

    private String className;

    private String packageName;

    public void addCodeBlock(CodeBlock codeBlock) {
        codeBlocks.add(codeBlock);
    }

    public MethodAdapter(String javaFile) {
        this.filePath = javaFile;
        this.compilationUnitParseResult = VisitorHelper.parseFile(filePath);
        CompilationUnit compilationUnit = VisitorHelper.loadCompilationUnit(this.compilationUnitParseResult);
        this.imports = VisitorHelper.getImports(compilationUnit);
        this.className = ParserUtils.getClassName(this.filePath);
        if (compilationUnit.getPackageDeclaration().isPresent())
            this.packageName = compilationUnit.getPackageDeclaration().get().getName().asString();
        for (TypeDeclaration typeDeclaration: compilationUnit.getTypes()) {
            parse(typeDeclaration);
        }
    }

    public List<CodeBlock> getCodeBlocks() {
        return codeBlocks;
    }

    private void parse(TypeDeclaration typeDeclaration) {
        if (!(typeDeclaration instanceof ClassOrInterfaceDeclaration))
            return;
        ClassOrInterfaceDeclaration classOrInterfaceDeclaration = (ClassOrInterfaceDeclaration) typeDeclaration;
        if (classOrInterfaceDeclaration.isInterface() || classOrInterfaceDeclaration.isAbstract())
            return;
        String typeName = classOrInterfaceDeclaration.getNameAsString();
        for (Object member: classOrInterfaceDeclaration.getMembers()) {
            if (member instanceof MethodDeclaration) {
                this.visit((MethodDeclaration) member, typeName);
            } else if (member instanceof TypeDeclaration) {
                this.parse((TypeDeclaration) member);
            }
        }
    }

    public void visit(MethodDeclaration methodDeclaration, Object parentClassName) {
        if (!methodDeclaration.getBody().isPresent() || methodDeclaration.isAbstract())
            return;
        CodeBlock codeBlock = new CodeBlock();
        codeBlock.setLanguage(Settings.LANGUAGE_JAVA);
        codeBlock.setSourceFile(this.filePath);
        codeBlock.setCode(VisitorHelper.removeComments(methodDeclaration));
        codeBlock.setComments(VisitorHelper.getAllComments(methodDeclaration));
        codeBlock.setImports(this.imports);
        codeBlock.setStatic(methodDeclaration.isStatic());
        codeBlock.setMethod(true);
        codeBlock.setFileClassName(this.className);
        codeBlock.setParentClassName(parentClassName.toString());
        codeBlock.setProjectSourcePath(ProjectConfig.TARGET_SOURCE);
        codeBlock.setProjectLangFolder(ProjectConfig.JAVA_FOLDER);
        codeBlock.setPackageName(this.packageName);
        addCodeBlock(codeBlock);
    }

}


public class MethodCrawl {

    private final static Logger LOGGER = Logger.getLogger(MethodCrawl.class.getName());

    private final static String TEMP_FOLDER = Utils.pathJoin(ProjectConfig.CODESEER_HOME, "code", "_temp");

    private final static File JAVA_TREE_FOLDER = new File(Utils.pathJoin(ProjectConfig.CODESEER_HOME, "code", "src", "main", "python"));

    private final static String BASE_CMD = "python mos/search/tree/java_tree.py";

    private final static CodeStore CODE_STORE = new CodeStore();

    public static void generateForFile(String filePath) {
        LOGGER.info(String.format("Processing file '%s' ... ", Utils.getRepoLocalPath(filePath)));
        CODE_STORE.deleteCodeBlockFromFile(filePath);
        MethodAdapter adapter = new MethodAdapter(filePath);
        List<CodeBlock> codeBlocks = adapter.getCodeBlocks();
        LOGGER.info(String.format("Updating contexts and AST for '%d' functions .... ", codeBlocks.size()));
        int contextsFound = 0, astsFound = 0;
        for (CodeBlock codeBlock: codeBlocks) {
            if (MethodCrawl.updateContextTokens(codeBlock))
                contextsFound++;
            if (MethodCrawl.getGenericAst(codeBlock))
                astsFound++;
            CODE_STORE.saveCodeBlock(codeBlock);
        }
        LOGGER.info(String.format("Contexts found for %d/%d ... ", contextsFound, codeBlocks.size()));
        LOGGER.info(String.format("ASTs found for %d/%d ... ", astsFound, codeBlocks.size()));
    }

    public static boolean updateContextTokens(CodeBlock codeBlock) {
        Set<String> tokens = Contexter.tokenize(codeBlock.getCode());
        String className = codeBlock.getParentClassName();
        if (className != null && !className.startsWith(Settings.GENERATED_FUNCTION_PREFIX))
            tokens.addAll(Contexter.tokenize(className));
        if (codeBlock.getComments() != null)
            tokens.addAll(Contexter.tokenize(codeBlock.getComments()));
        if (tokens != null && tokens.size() > 0)
            codeBlock.setContextualTokens(tokens);
        return tokens != null && tokens.size() > 0;
    }

    public static boolean getGenericAst(CodeBlock codeBlock) {
        String file_name = Utils.pathJoin(TEMP_FOLDER, String.format("%s.txt", codeBlock.getUid()));
        Utils.writeFileContent(codeBlock.getCode(), file_name);
        String cmd = String.format("%s %s true", BASE_CMD, file_name);
        boolean astStatus = false;
        try {
            Process process = Runtime.getRuntime().exec(cmd, null, JAVA_TREE_FOLDER);
            process.waitFor();
            String contents = Utils.readFromFile(file_name);
            if (contents.startsWith("Error")) {
                LOGGER.severe(String.format("Error in file: \n%s", codeBlock.getCode().trim()));
                LOGGER.severe(contents);
            } else {
                astStatus = true;
                codeBlock.setAst(contents.trim());
            }
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        } finally {
            Utils.deleteFileOrFolder(file_name);
        }
        return astStatus;
    }

    public static void main(String[] args) {
        String fName = "/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/commons-lang/src/main/java/org/apache/commons/lang3/StringUtils.java";
        generateForFile(fName);
    }

}
