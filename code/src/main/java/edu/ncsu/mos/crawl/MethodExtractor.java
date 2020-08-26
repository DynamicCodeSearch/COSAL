package edu.ncsu.mos.crawl;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.TypeDeclaration;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.mos.blocks.CodeBlock;
import edu.ncsu.mos.helpers.Contexter;
import edu.ncsu.mos.rest.ASTParser;
import edu.ncsu.mos.store.CodeStore;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.logging.Logger;

public class MethodExtractor extends VoidVisitorAdapter {

    private static final Logger LOGGER = Logger.getLogger(MethodExtractor.class.getName());

    private CompilationUnit compilationUnit;

    private final static CodeStore CODE_STORE = new CodeStore();

    private CodeBlock fileBlock;

    private List<CodeBlock> functionBlocks = new ArrayList<>();

    public List<CodeBlock> getFunctionBlocks() {
        return functionBlocks;
    }

    public MethodExtractor(String sourceCodePath) {
        fileBlock = CODE_STORE.getFileBlock(sourceCodePath);
        if (fileBlock == null)
            return;
        String contents = Utils.readFromFile(sourceCodePath);
        compilationUnit = VisitorHelper.parseContent(contents);
        for (TypeDeclaration typeDeclaration: compilationUnit.getTypes())
            parse(typeDeclaration);
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
        codeBlock.setSourceFile(fileBlock.getSourceFile());
        codeBlock.setCode(VisitorHelper.removeComments(methodDeclaration));
        codeBlock.setComments(VisitorHelper.getAllComments(methodDeclaration));
        codeBlock.setImports(fileBlock.getImports());
        codeBlock.setStatic(methodDeclaration.isStatic());
        codeBlock.setMethod(true);
        codeBlock.setFileClassName(fileBlock.getFileClassName());
        codeBlock.setParentClassName(parentClassName.toString());
        codeBlock.setProjectSourcePath(fileBlock.getProjectSourcePath());
        codeBlock.setProjectLangFolder(fileBlock.getProjectLangFolder());
        codeBlock.setAst(ASTParser.getJavaASTForFunction(codeBlock.getCode()));
        codeBlock.setContextualTokens(getContextTokens(codeBlock));
        codeBlock.setContestMeta(fileBlock.getContestMeta());
        functionBlocks.add(codeBlock);
    }

    private static Set<String> getContextTokens(CodeBlock codeBlock) {
        Set<String> tokens = Contexter.tokenize(codeBlock.getCode());
        String className = codeBlock.getParentClassName();
        if (className != null && !className.startsWith(Settings.GENERATED_FUNCTION_PREFIX))
            tokens.addAll(Contexter.tokenize(className));
        if (codeBlock.getComments() != null)
            tokens.addAll(Contexter.tokenize(codeBlock.getComments()));
        if (tokens != null && tokens.size() > 0)
            return tokens;
        return null;
    }

    public static void extractMethodsForFile(String filePath) {
        CODE_STORE.deleteCodeBlockFromFile(filePath);
        MethodExtractor extractor = new MethodExtractor(filePath);
        List<CodeBlock> functionBlocks = extractor.getFunctionBlocks();
        for (CodeBlock functionBlock: functionBlocks)
            CODE_STORE.saveCodeBlock(functionBlock);
    }


    public static void extractMethods() {
        int index = 0;
        List<String> sourceFiles = Utils.listNonGeneratedJavaFiles(ProjectConfig.PROJECTS_JAVA_FOLDER);
        for (String filePath: sourceFiles) {
            if (index % 100 == 0)
                LOGGER.info(String.format("Processing file %d/%d ... ", index + 1, sourceFiles.size()));
            extractMethodsForFile(filePath);
            index += 1;
        }
    }


    public static void test() {
        String javaFilePath = "/Users/panzer/Raise/ProgramRepair/CodeSeer/subjects/atcoder/src/main/java/C19/P0/S1140549/Main.java";
        extractMethodsForFile(javaFilePath);
    }

    public static void main(String[] args) {
        extractMethods();
    }

}
