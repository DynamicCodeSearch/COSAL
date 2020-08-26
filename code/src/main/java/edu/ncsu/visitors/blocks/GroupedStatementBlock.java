package edu.ncsu.visitors.blocks;

import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.stmt.*;

import java.util.ArrayList;
import java.util.List;

import edu.ncsu.visitors.helpers.StatementHelper;

public class GroupedStatementBlock extends StatementBlock{

    /***
     * List of statement blocks in a group of statement blocks
     */
    protected List<StatementBlock> statementBlocks;

    /***
     * List of statement blocks in a grouped statement block
     * @return
     */
    public List<StatementBlock> getStatementBlocks() {
        return statementBlocks;
    }


    /***
     * @param fileSource Path of class file
     * @param parentClass Class name of parent
     * @param methodName Name of the method
     * @param statementAST AST of statement
     * @param parentStatement StatementBlock pointing to the parent
     */
    public GroupedStatementBlock(String fileSource, String parentClass, String methodName, Node statementAST, StatementBlock parentStatement) {
        super(fileSource, parentClass, methodName, statementAST, parentStatement);
        statementBlocks = new ArrayList<>();
        if (statementAST instanceof BlockStmt) {
            List<Statement> statements = ((BlockStmt) statementAST).getStatements();
            for (Statement statement: statements) {
                StatementBlock stmtBlock = StatementHelper.parseStatementNode(fileSource, parentClass, methodName, statement, this);
                if (stmtBlock != null)
                    statementBlocks.add(stmtBlock);
            }
        } else if (statementAST instanceof DoStmt) {
            StatementBlock stmtBlock = StatementHelper.parseStatementNode(fileSource, parentClass,
                    methodName, ((DoStmt) statementAST).getBody(), this);
            if (stmtBlock != null)
                statementBlocks.add(stmtBlock);
        } else if (statementAST instanceof ForEachStmt) {
            StatementBlock stmtBlock = StatementHelper.parseStatementNode(fileSource, parentClass,
                    methodName, ((ForEachStmt) statementAST).getBody(), this);
            if (stmtBlock != null)
                statementBlocks.add(stmtBlock);
        } else if (statementAST instanceof ForStmt) {
            StatementBlock stmtBlock = StatementHelper.parseStatementNode(fileSource, parentClass,
                    methodName, ((ForStmt) statementAST).getBody(), this);
            if (stmtBlock != null)
                statementBlocks.add(stmtBlock);
        }
//        else if (statementAST instanceof IfStmt) {
//            IfStmt ifStmt = (IfStmt) statementAST;
//            statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
//                    methodName, ifStmt.getThenStmt()));
//
//            if (ifStmt.getElseStmt() != null) {
//                statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
//                        methodName, ((IfStmt) statementAST).getElseStmt()));
//            }
//        }
        else if (statementAST instanceof LabeledStmt) {
            StatementBlock stmtBlock = StatementHelper.parseStatementNode(fileSource, parentClass,
                    methodName, ((LabeledStmt) statementAST).getStatement(), this);
            if (stmtBlock != null)
                statementBlocks.add(stmtBlock);
        }
//        else if (statementAST instanceof SwitchStmt) {
//            for (Statement entry: ((SwitchStmt) statementAST).getEntries()) {
//                statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
//                        methodName, entry));
//            }
//        }
        else if (statementAST instanceof SwitchEntry) {
            for (Statement statement: ((SwitchEntry) statementAST).getStatements()) {
                StatementBlock stmtBlock = StatementHelper.parseStatementNode(fileSource, parentClass,
                        methodName, statement, this);
                if (stmtBlock != null)
                    statementBlocks.add(stmtBlock);
            }
        } else if (statementAST instanceof TryStmt) {
            StatementBlock stmtBlock = StatementHelper.parseStatementNode(fileSource, parentClass, methodName,
                    ((TryStmt) statementAST).getTryBlock(), this);
            if (stmtBlock != null)
                statementBlocks.add(stmtBlock);
        } else if (statementAST instanceof  WhileStmt) {
            StatementBlock stmtBlock = StatementHelper.parseStatementNode(fileSource, parentClass,
                    methodName, ((WhileStmt) statementAST).getBody(), this);
            if (stmtBlock != null)
                statementBlocks.add(stmtBlock);
        }
    }

    @Override
    public String toString() {
        return super.toStringHelper()
                .add("statements", statementBlocks)
                .toString();
    }
}
