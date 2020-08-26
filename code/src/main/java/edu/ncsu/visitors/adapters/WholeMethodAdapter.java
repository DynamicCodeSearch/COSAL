package edu.ncsu.visitors.adapters;

import com.github.javaparser.ParseResult;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.TypeDeclaration;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import edu.ncsu.config.Settings;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.blocks.GeneratedFunction;
import edu.ncsu.visitors.helpers.Constants;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

public class WholeMethodAdapter extends VoidVisitorAdapter {

    private static final Logger LOGGER = Logger.getLogger(WholeMethodAdapter.class.getName());

    private String dataset;

    private ParseResult<CompilationUnit> compilationUnitParseResult;

    private String fileName;

    private String generatedFile;

    private List<GeneratedFunction> generatedFunctions;

    public CompilationUnit getCompilationUnit() {
        return VisitorHelper.loadCompilationUnit(compilationUnitParseResult);
    }

    public WholeMethodAdapter(String dataset, String javaFile) {
        this.dataset = dataset;
        this.fileName = javaFile;
        this.compilationUnitParseResult = VisitorHelper.parseFile(javaFile);
        CompilationUnit compilationUnit = VisitorHelper.loadCompilationUnit(compilationUnitParseResult);
        String generatedClassName = Settings.GENERATED_CLASS_PREFIX + Utils.randomString();
        String packageName = VisitorHelper.getPackage(compilationUnit);
        String writePath = Utils.pathJoin(Settings.PROJECTS_BASE_JAVA_FOLDER, packageName.replaceAll("\\.", File.separator));
        this.generatedFile = Utils.pathJoin(writePath, generatedClassName + ".java");
        this.generatedFunctions = new ArrayList<>();
        visit(compilationUnit, null);
    }

    private ClassOrInterfaceDeclaration getParentClass(Node node) {
        if (node instanceof ClassOrInterfaceDeclaration)
            return (ClassOrInterfaceDeclaration) node;
        Node currentNode = node;
        while (currentNode.getParentNode().isPresent()) {
            currentNode = currentNode.getParentNode().get();
            if (currentNode instanceof ClassOrInterfaceDeclaration)
                return (ClassOrInterfaceDeclaration) currentNode;
        }
        return null;
    }

    public void visit(MethodDeclaration methodDeclaration, Object arg) {
        GeneratedFunction generatedFunction = new GeneratedFunction();
        generatedFunction.setName("func_" + Utils.randomString());
        generatedFunction.setSourceCodeFunctionName(methodDeclaration.getNameAsString());
        ClassOrInterfaceDeclaration parentClass = getParentClass(methodDeclaration);
        if (parentClass != null)
            generatedFunction.setSourceCodeClassName(parentClass.getNameAsString());
        generatedFunction.setWholeMethod(true);
        generatedFunction.setBody(methodDeclaration.toString());
        generatedFunction.setSourceFile(fileName);
        generatedFunction.setGeneratedFile(generatedFile);
        generatedFunctions.add(generatedFunction);
    }

    public List<GeneratedFunction> getGeneratedFunctions() {
        return generatedFunctions;
    }

    public String getMainClassName() {
        for (TypeDeclaration type: getCompilationUnit().getTypes()) {
            if (VisitorHelper.getScopeModifier(type.getModifiers()).equals(Constants.PUBLIC))
                return type.getNameAsString();
        }
        return null;
    }
}
