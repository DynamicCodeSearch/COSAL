package edu.ncsu.haskell.parser;

import edu.ncsu.haskell.parser.antlr.HaskellLexer;
import edu.ncsu.haskell.parser.antlr.HaskellParser;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.Predicate;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.TerminalNodeImpl;
import org.antlr.v4.runtime.tree.Tree;
import org.antlr.v4.runtime.tree.Trees;

import java.util.Arrays;
import java.util.List;


class FunctionNodePredicate implements Predicate<ParseTree> {
    @Override
    public boolean test(ParseTree tree) {
        if (tree instanceof TerminalNodeImpl) {
            return false;
        }
        String name = TreeUtils.getAntlrNodeName(tree);
        return name.toLowerCase().equals("decl_no_th");
    }
}

public class AntlrParser {



    public static void main(String[] args) {
        String haskellCode = "in_range min max x = x >= min && x <= max";
        CharStream input = CharStreams.fromString(haskellCode);
        HaskellLexer lexer = new HaskellLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        HaskellParser parser = new HaskellParser(tokens);
        RuleContext tree = parser.module();
        Predicate p = new FunctionNodePredicate();
        System.out.println(TreeUtils.toJson(tree));
        Tree funcTree = Trees.findNodeSuchThat(tree, p);
        System.out.println(TreeUtils.toJson(funcTree));


//        List<String> ruleNamesList = Arrays.asList(parser.getRuleNames());
//        String parseTree = TreeUtils.toPrettyTree(tree, ruleNamesList);
//        System.out.println(parseTree);
    }

}
