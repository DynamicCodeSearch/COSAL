package edu.ncsu.visitors.helpers;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ParseResult;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.ImportDeclaration;
import com.github.javaparser.ast.Modifier;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.TypeDeclaration;
import com.github.javaparser.ast.comments.Comment;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.nodeTypes.NodeWithName;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import edu.ncsu.visitors.blocks.*;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Optional;

public class VisitorHelper {

    /***
     * Load the ast compilation unit of the java source file.
     * @param sourceCode - Source code as text
     * @return - Compilation unit of the source file
     */
    public static ParseResult<CompilationUnit> parseSourceCode(String sourceCode) {
        JavaParser parser = new JavaParser();
        return parser.parse(sourceCode);
    }

    /***
     * Load the ast compilation unit of the java source file.
     * @param javaFilePath - Path of the java file.
     * @return - Compilation unit of the source file
     */
    public static ParseResult<CompilationUnit> parseFile(String javaFilePath) {
        File srcFile = new File(javaFilePath);
        JavaParser parser = new JavaParser();
        try {
            return parser.parse(srcFile);
        } catch (IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    /***
     * Load the ast compilation unit of java source code.
     * @param sourceCode - Java Source Code
     * @return - Parsed compilation unit.
     */
    public static CompilationUnit parseContent(String sourceCode) {
        JavaParser parser = new JavaParser();
        ParseResult<CompilationUnit> result = parser.parse(sourceCode);
        return loadCompilationUnit(result);
    }

    /***
     * Get primary class name
     * @param compilationUnit - Instance of class name
     * @return - Name of the primary class
     */
    public static String getMainClassName(CompilationUnit compilationUnit) {
        String mainClassName = null;
        for (TypeDeclaration typeDeclaration: compilationUnit.getTypes()) {
            if (getScopeModifier(typeDeclaration.getModifiers()).equals(Constants.PUBLIC))
                mainClassName = typeDeclaration.getNameAsString();
            else if (mainClassName == null)
                mainClassName = typeDeclaration.getNameAsString();
        }
        return mainClassName;
    }

    public static CompilationUnit loadCompilationUnit(ParseResult<CompilationUnit> parseResult) {
        if (parseResult.isSuccessful()) {
            Optional<CompilationUnit> maybeCompilationUnit = parseResult.getResult();
            if (maybeCompilationUnit.isPresent()) {
                return maybeCompilationUnit.get();
            }
            throw new RuntimeException("Compilation unit is empty");
        }
        String message = parseResult.toString();
        throw new RuntimeException(message);
    }

    /***
     * @return name of the package in compilation unit
     */
    public static String getPackage(CompilationUnit compilationUnit) {
        return compilationUnit.getPackageDeclaration().map(NodeWithName::getNameAsString).orElse(null);
    }

    @SuppressWarnings("unchecked")
    public static void visit(VoidVisitorAdapter adapter, Expression expression, Object arg) {
        if (expression instanceof ArrayAccessExpr) {
            adapter.visit((ArrayAccessExpr) expression, arg);
        } else if (expression instanceof ArrayCreationExpr) {
            adapter.visit((ArrayCreationExpr) expression, arg);
        } else if (expression instanceof ArrayInitializerExpr) {
            adapter.visit((ArrayInitializerExpr) expression, arg);
        } else if (expression instanceof AssignExpr) {
            adapter.visit((AssignExpr) expression, arg);
        } else if (expression instanceof BinaryExpr) {
            adapter.visit((BinaryExpr) expression, arg);
        } else if (expression instanceof BooleanLiteralExpr) {
            adapter.visit((BooleanLiteralExpr) expression, arg);
        } else if (expression instanceof CastExpr) {
            adapter.visit((CastExpr) expression, arg);
        } else if (expression instanceof CharLiteralExpr) {
            adapter.visit((CharLiteralExpr) expression, arg);
        } else if (expression instanceof ClassExpr) {
            adapter.visit((ClassExpr) expression, arg);
        } else if (expression instanceof ConditionalExpr) {
            adapter.visit((ConditionalExpr) expression, arg);
        } else if (expression instanceof DoubleLiteralExpr) {
            adapter.visit((DoubleLiteralExpr) expression, arg);
        } else if (expression instanceof EnclosedExpr) {
            adapter.visit((EnclosedExpr) expression, arg);
        } else if (expression instanceof FieldAccessExpr) {
            adapter.visit((FieldAccessExpr) expression, arg);
        } else if (expression instanceof InstanceOfExpr) {
            adapter.visit((InstanceOfExpr) expression, arg);
        } else if (expression instanceof IntegerLiteralExpr) {
            adapter.visit((IntegerLiteralExpr) expression, arg);
        } else if (expression instanceof LambdaExpr) {
            adapter.visit((LambdaExpr) expression, arg);
        } else if (expression instanceof LongLiteralExpr) {
            adapter.visit((LongLiteralExpr) expression, arg);
        } else if (expression instanceof MarkerAnnotationExpr) {
            adapter.visit((MarkerAnnotationExpr) expression, arg);
        } else if (expression instanceof MethodCallExpr) {
            adapter.visit((MethodCallExpr) expression, arg);
        } else if (expression instanceof MethodReferenceExpr) {
            adapter.visit((MethodReferenceExpr) expression, arg);
        } else if (expression instanceof NameExpr) {
            adapter.visit((NameExpr) expression, arg);
        } else if (expression instanceof NormalAnnotationExpr) {
            adapter.visit((NormalAnnotationExpr) expression, arg);
        } else if (expression instanceof NullLiteralExpr) {
            adapter.visit((NullLiteralExpr) expression, arg);
        } else if (expression instanceof ObjectCreationExpr) {
            adapter.visit((ObjectCreationExpr) expression, arg);
        } else if (expression instanceof SingleMemberAnnotationExpr) {
            adapter.visit((SingleMemberAnnotationExpr) expression, arg);
        } else if (expression instanceof StringLiteralExpr) {
            adapter.visit((StringLiteralExpr) expression, arg);
        } else if (expression instanceof SuperExpr) {
            adapter.visit((SuperExpr) expression, arg);
        } else if (expression instanceof ThisExpr) {
            adapter.visit((ThisExpr) expression, arg);
        } else if (expression instanceof TypeExpr) {
            adapter.visit((TypeExpr) expression, arg);
        } else if (expression instanceof UnaryExpr) {
            adapter.visit((UnaryExpr) expression, arg);
        } else if (expression instanceof VariableDeclarationExpr) {
            adapter.visit((VariableDeclarationExpr) expression, arg);
        }
    }

    public static void updateVariableUsage(String variableName, VariablePosition position,
                                           MethodBlock methodBlock, ClassBlock classBlock, boolean updateAssign) {
        Map<String, Variable> fieldVariableMap = classBlock.getFieldVariables();
        boolean variableFound = false;
        if (methodBlock.getVariableDeclareMap() != null && methodBlock.getVariableDeclareMap().containsKey(variableName)){
            variableFound = methodBlock.updateVariableUsage(variableName, position, updateAssign);
        }
        if (!variableFound && fieldVariableMap.containsKey(variableName)) {
            Variable fieldVariable = fieldVariableMap.get(variableName);
            fieldVariable.insertAssignPosition(position);
            fieldVariable.insertUsedPosition(position);
            fieldVariableMap.put(variableName, fieldVariable);
        }
    }

    public static String getScopeModifier(List<Modifier> modifiers) {
        for (Modifier modifier : modifiers) {
            if (modifier.getKeyword().equals(Modifier.Keyword.PUBLIC)) {
                return Constants.PUBLIC;
            } else if (modifier.getKeyword().equals(Modifier.Keyword.PROTECTED)) {
                return Constants.PROTECTED;
            } else if (modifier.getKeyword().equals(Modifier.Keyword.PRIVATE)) {
                return Constants.PRIVATE;
            }
        }
        return Constants.DEFAULT;
    }

    public static boolean isStatic(List<Modifier> modifiers) {
        for (Modifier modifier: modifiers) {
            if (modifier.getKeyword().equals(Modifier.Keyword.STATIC))
                return true;
        }
        return false;
    }

    public static boolean isAbstract(List<Modifier> modifiers) {
        for (Modifier modifier: modifiers) {
            if (modifier.getKeyword().equals(Modifier.Keyword.ABSTRACT))
                return true;
        }
        return false;
    }

    public static boolean isScope(List<Modifier> modifiers, Modifier.Keyword keyword) {
        for (Modifier modifier: modifiers) {
            if (modifier.getKeyword().equals(keyword))
                return true;
        }
        return false;
    }

    public static void removeModifier(List<Modifier> modifiers, Modifier.Keyword keyword) {
        for (Modifier modifier: modifiers) {
            if (modifier.getKeyword().equals(keyword))
                modifiers.remove(modifier);
        }
    }

    public static List<ImportBlock> getImports(CompilationUnit compilationUnit) {
        List<ImportBlock> imports = new ArrayList<>();
        for (ImportDeclaration importDeclaration: compilationUnit.getImports()) {
            imports.add(new ImportBlock(importDeclaration));
        }
        return imports;
    }

    public static String getAllComments(MethodDeclaration methodDeclaration) {
        StringBuilder comments = new StringBuilder();
        if (methodDeclaration.getJavadoc().isPresent()) {
            comments.append(methodDeclaration.getJavadoc().get().toText()).append("\n");
        }
        List<Comment> allComments = methodDeclaration.getAllContainedComments();
        for (Comment comment: allComments)
            comments.append(comment.getContent()).append("\n");
        if (comments.length() > 0)
            return comments.toString().trim();
        return null;
    }

    public static String removeComments(Node node) {
        return node.toString().replaceAll("/\\*[^*]*(?:\\*(?!/)[^*]*)*\\*/|//.*", "");
    }

}
