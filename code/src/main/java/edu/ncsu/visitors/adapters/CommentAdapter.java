package edu.ncsu.visitors.adapters;

import com.github.javaparser.ParseResult;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.comments.BlockComment;
import com.github.javaparser.ast.comments.Comment;
import com.github.javaparser.ast.comments.JavadocComment;
import com.github.javaparser.ast.comments.LineComment;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class CommentAdapter extends VoidVisitorAdapter {

    private String javaFile;

    private Set<Integer> nonSourceCodeLineNumbers = new HashSet<>();

    private ParseResult<CompilationUnit> compilationUnitParseResult;

    private List<String> lines;

    public CommentAdapter(String javaFile) {
        this.javaFile = javaFile;
        this.compilationUnitParseResult = VisitorHelper.parseFile(javaFile);
        initialize();
    }

    public CommentAdapter(String javaFile, ParseResult<CompilationUnit> compilationUnitParseResult) {
        this.javaFile = javaFile;
        this.compilationUnitParseResult = compilationUnitParseResult;
        initialize();
    }

    private void initialize() {
        lines = Utils.readLinesFromFile(javaFile);
        if (lines != null) {
            int i = 1;
            for (String line: lines) {
                if (line.replaceAll("\\s+", "").length() == 0) {
                    nonSourceCodeLineNumbers.add(i);
                }
                i += 1;
            }
        }
        for (Comment comment: VisitorHelper.loadCompilationUnit(compilationUnitParseResult).getComments()) {
            if (comment instanceof LineComment) {
                visit((LineComment) comment, null);
            } else if (comment instanceof BlockComment) {
                visit((BlockComment) comment, null);
            } else if (comment instanceof JavadocComment) {
                visit((JavadocComment) comment, null);
            }
        }
    }

    @Override
    public void visit(LineComment n, Object arg) {
        if (!n.getBegin().isPresent())
            return;
        int lineNumber =  n.getBegin().get().line;
        String line = lines.get(lineNumber - 1);
        if (line.replaceAll("\\s+", "").startsWith("//"))
            nonSourceCodeLineNumbers.add(lineNumber);
    }

    @Override
    public void visit(BlockComment n, Object arg) {
        if (!n.getBegin().isPresent() || !n.getEnd().isPresent())
            return;
        int beginLine = n.getBegin().get().line;
        int endLine = n.getEnd().get().line;
        for (int i=beginLine; i <= endLine; i++)
            nonSourceCodeLineNumbers.add(i);
    }

    @Override
    public void visit(JavadocComment n, Object arg) {
        if (!n.getBegin().isPresent() || !n.getEnd().isPresent())
            return;
        int beginLine = n.getBegin().get().line;
        int endLine = n.getEnd().get().line;
        for (int i=beginLine; i <= endLine; i++)
            nonSourceCodeLineNumbers.add(i);
    }

    public Set<Integer> getSourceCodeLines() {
        CompilationUnit compilationUnit = VisitorHelper.loadCompilationUnit(compilationUnitParseResult);
        if (!compilationUnit.getBegin().isPresent() || !compilationUnit.getEnd().isPresent())
            return null;
        int startLine = compilationUnit.getBegin().get().line;
        int endLine = compilationUnit.getEnd().get().line;
        Set<Integer> sourceCodeLines = new HashSet<>();
        for (int i=startLine; i <= endLine; i++) {
            if (!nonSourceCodeLineNumbers.contains(i))
                sourceCodeLines.add(i);
        }
        return sourceCodeLines;
    }

}
