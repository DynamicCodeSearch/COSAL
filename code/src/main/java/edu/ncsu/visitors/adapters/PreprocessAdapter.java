package edu.ncsu.visitors.adapters;

import com.github.javaparser.ParseResult;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.Modifier;
import com.github.javaparser.ast.NodeList;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import edu.ncsu.utils.InMemoryJavaCompiler;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.util.logging.Logger;

public class PreprocessAdapter extends VoidVisitorAdapter {
    private static final Logger LOGGER = Logger.getLogger(PreprocessAdapter.class.getName());

    private String fileName;

    private ParseResult<CompilationUnit> compilationUnitParseResult;

    public static void preprocess(String javaFile) {
        String oldSource = Utils.getFileContent(javaFile);
        PreprocessAdapter adapter = new PreprocessAdapter(javaFile);
        String newSource = VisitorHelper.loadCompilationUnit(adapter.compilationUnitParseResult).toString();
        Utils.writeFileContent(newSource, adapter.fileName);
        if (!InMemoryJavaCompiler.compile(adapter.fileName, false)) {
            LOGGER.warning(String.format("Preprocessed file '%s' raises compilation error. " +
                    "Reverting to old content ... ", adapter.fileName));
            Utils.writeFileContent(oldSource, adapter.fileName);
        } else {
            LOGGER.info(String.format("Preprocessed file '%s'.", adapter.fileName));
        }
    }

    private PreprocessAdapter(String javaFile) {
        this.fileName = javaFile;
        this.compilationUnitParseResult = VisitorHelper.parseFile(javaFile);
        for (TypeDeclaration typeDeclaration: VisitorHelper.loadCompilationUnit(compilationUnitParseResult).getTypes()) {
            if (typeDeclaration instanceof ClassOrInterfaceDeclaration) {
                parseTypeDeclaration((ClassOrInterfaceDeclaration) typeDeclaration, false);
            }
        }
    }

    private void parseTypeDeclaration(ClassOrInterfaceDeclaration typeDeclaration, boolean isInner) {
        NodeList<Modifier> classModifiers = typeDeclaration.getModifiers();
        if (isInner && !VisitorHelper.isStatic(classModifiers)) {
            classModifiers.add(Modifier.staticModifier());
            typeDeclaration.setModifiers(classModifiers);
        }
        for (BodyDeclaration member: typeDeclaration.getMembers()) {
            if (member instanceof FieldDeclaration) {
                FieldDeclaration declaration = (FieldDeclaration) member;
                NodeList<Modifier> fieldModifiers = typeDeclaration.getModifiers();
                if (VisitorHelper.isScope(fieldModifiers, Modifier.Keyword.PRIVATE)) {
                    VisitorHelper.removeModifier(fieldModifiers, Modifier.Keyword.PRIVATE);
                    declaration.setModifiers(fieldModifiers);
                }
            } else if (member instanceof MethodDeclaration) {
                MethodDeclaration declaration = (MethodDeclaration) member;
                NodeList<Modifier> methodModifiers = declaration.getModifiers();
                if (VisitorHelper.isScope(methodModifiers, Modifier.Keyword.PRIVATE)) {
                    VisitorHelper.removeModifier(methodModifiers, Modifier.Keyword.PRIVATE);
                    declaration.setModifiers(methodModifiers);
                }
            } else if (member instanceof ClassOrInterfaceDeclaration){
                parseTypeDeclaration((ClassOrInterfaceDeclaration) member, true);
            }
        }
    }

    private static void testPreprocess() {
        String fileName = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/stupid/Dummy.java";
        preprocess(fileName);
    }

    public static void main(String[] args) {
        testPreprocess();
    }

}
