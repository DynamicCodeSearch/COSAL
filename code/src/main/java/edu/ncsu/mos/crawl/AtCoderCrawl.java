package edu.ncsu.mos.crawl;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import edu.ncsu.mos.blocks.CodeBlock;
import edu.ncsu.mos.blocks.ContestMeta;
import edu.ncsu.mos.store.CodeStore;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.blocks.ImportBlock;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.sql.*;
import java.util.List;
import java.util.logging.Logger;

class AtCoderAdapter extends VoidVisitorAdapter {

    private CompilationUnit compilationUnit;

    private ContestMeta contestMeta;

    private List<ImportBlock> imports;

    private String filePath;

    private String packageName;

    private String className;

    public AtCoderAdapter(String sourceCode, ContestMeta contestMeta) {
        this.compilationUnit = VisitorHelper.parseContent(sourceCode);
        this.contestMeta = contestMeta;
        parse();
    }

    public AtCoderAdapter parse() {
        this.imports = VisitorHelper.getImports(this.compilationUnit);
        className = VisitorHelper.getMainClassName(this.compilationUnit);
        packageName = String.format("C%d.P%d.S%d", contestMeta.contestId, contestMeta.problemId, contestMeta.submissionId);
        compilationUnit = compilationUnit.setPackageDeclaration(packageName);
        filePath = Utils.pathJoin(Utils.pathJoin(packageName.split("\\.")), String.format("%s.java", className));
        return this;
    }

    public String getSource() {
        return compilationUnit.toString();
    }

    public String getFilePath() {
        return filePath;
    }

    public List<ImportBlock> getImports() {
        return imports;
    }

    public String getPackageName() {
        return packageName;
    }

    public String getClassName() {
        return className;
    }
}


public class AtCoderCrawl {

    private final static Logger LOGGER = Logger.getLogger(AtCoderCrawl.class.getName());

    private final static String DB_PATH = Utils.pathJoin(ProjectConfig.CODESEER_HOME, "atcoder", "java-python-clones.db");

    private final static CodeStore CODE_STORE = new CodeStore();

    private static Connection connect() {
        try {
            return DriverManager.getConnection(String.format("jdbc:sqlite:%s", DB_PATH));
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    private static String getString(ResultSet rs, String attribute) {
        try {
            return rs.getString(attribute);
        } catch (SQLException e) {
            return null;
        }
    }

    private static long getLong(ResultSet rs, String attribute) {
        try {
            return rs.getLong(attribute);
        } catch (SQLException e) {
            return 0L;
        }
    }

    public static void processResultSet(ResultSet rs) {
        CodeBlock block = new CodeBlock();
        block.setLanguage(Settings.LANGUAGE_JAVA);
        block.setSourceFile(getString(rs, "filename"));
        block.setFile(true);
        block.setProjectLangFolder(ProjectConfig.PROJECTS_JAVA_FOLDER);
        block.setProjectSourcePath(ProjectConfig.TARGET_SOURCE);
        ContestMeta contestMeta = new ContestMeta();
        contestMeta.setSubmissionId(getLong(rs, "id"));
        contestMeta.setContestType(getString(rs, "contest_type"));
        contestMeta.setContestId(getLong(rs, "contest_id"));
        contestMeta.setProblemId(getLong(rs, "problem_id"));
        contestMeta.setCodeSize(getLong(rs, "source_length"));
        contestMeta.setExecTime(getLong(rs, "exec_time"));
        block.setContestMeta(contestMeta);
        AtCoderAdapter atCoderAdapter = new AtCoderAdapter(getString(rs, "source"), contestMeta);
        block.setCode(atCoderAdapter.getSource());
        block.setSourceFile(Utils.pathJoin(ProjectConfig.PROJECTS_JAVA_FOLDER, atCoderAdapter.getFilePath()));
        block.setImports(atCoderAdapter.getImports());
        block.setFileClassName(atCoderAdapter.getClassName());
        block.setPackageName(atCoderAdapter.getPackageName());
        // Saving file in projects.
        Utils.writeFileContent(block.getCode(), block.getSourceFile());
        // Saving file block in DB
        CODE_STORE.saveFileBlock(block);
    }

    private static void getSubmissions() {
        CODE_STORE.deleteAllFileBlocks();
        Utils.deleteFileOrFolder(ProjectConfig.PROJECTS_JAVA_FOLDER);
        try {
            Connection connection = connect();
            String countQuery =  "SELECT COUNT(*) AS cnt FROM submissions  WHERE language_code = ?";
            PreparedStatement stmt = connection.prepareStatement(countQuery);
            stmt.setString(1, "java");
            ResultSet resultSet = stmt.executeQuery();
            resultSet.next();
            long count = getLong(resultSet, "cnt");
            String  query = "SELECT * FROM submissions WHERE language_code = ?";
            stmt = connection.prepareStatement(query);
            stmt.setString(1, "java");
            resultSet = stmt.executeQuery();
            long start = System.currentTimeMillis();
            int index = 0;
            while (resultSet.next()) {
                index += 1;
                if (index % 1000 == 0)
                    LOGGER.info(String.format("Processing java file %d/%d ... ", index, count));
                processResultSet(resultSet);
            }
            long end = System.currentTimeMillis();
            double timeTaken = (end - start) / 1000.0;
            LOGGER.info(String.format("Time taken: %.4f secs", timeTaken));
        } catch (SQLException e) {
            throw  new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        getSubmissions();
    }

}
