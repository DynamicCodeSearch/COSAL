package edu.ncsu.visitors.blocks;

import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.stmt.IfStmt;
import com.github.javaparser.ast.stmt.SwitchEntry;
import com.github.javaparser.ast.stmt.SwitchStmt;
import edu.ncsu.visitors.helpers.StatementHelper;

import java.util.ArrayList;
import java.util.List;

public class ChoiceGroupedStatementBlock extends StatementBlock{

    /***
     * Optional set of StatementBlocks. Eg. If else, Switchcase
     */
    protected List<StatementBlock> statementBlocks;

    /***
     * @return Getter statementBlocks
     */
    public List<StatementBlock> getStatementBlocks() {
        return statementBlocks;
    }

    /***
     * Initialize ChoiceGroupedStatement
     * @param fileSource: Source of file
     * @param parentClass: Parent class
     * @param methodName: Name of method
     * @param statementAST: AST node of statement.
     * @param parentStatement: Parent statement block
     */
    public ChoiceGroupedStatementBlock(String fileSource, String parentClass, String methodName, Node statementAST, StatementBlock parentStatement) {
        super(fileSource, parentClass, methodName, statementAST, parentStatement);
        statementBlocks = new ArrayList<>();
        if (statementAST instanceof IfStmt) {
            IfStmt ifStmt = (IfStmt) statementAST;
            StatementBlock stmtBlock = StatementHelper.parseStatementNode(fileSource, parentClass,
                    methodName, ifStmt.getThenStmt(), this);
            if (stmtBlock != null)
                statementBlocks.add(stmtBlock);
            if (ifStmt.getElseStmt().isPresent()) {
                StatementBlock elseStmtBlock = StatementHelper.parseStatementNode(fileSource, parentClass,
                        methodName, ifStmt.getElseStmt().get(), this);
                if (elseStmtBlock != null)
                    statementBlocks.add(elseStmtBlock);
            }
        } else if (statementAST instanceof SwitchStmt) {
            for (SwitchEntry entry: ((SwitchStmt) statementAST).getEntries()) {
                StatementBlock stmtBlock = StatementHelper.parseStatementNode(fileSource, parentClass,
                        methodName, entry, this);
                if (stmtBlock != null)
                    statementBlocks.add(stmtBlock);
            }
        }
    }
}
