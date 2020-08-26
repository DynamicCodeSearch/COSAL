package edu.ncsu.config.project;

import edu.ncsu.utils.Utils;

public class IntroClassConfig extends BaseProjectConfig{
    @Override
    public String getProjectName() {
        return "IntroClassJava";
    }

    @Override
    public String getDataset() {
        return "IntroClassJava";
    }

    @Override
    public String getDatasetFolder() {
        return Utils.pathJoin("projects", getJavaFolder(), "IntroClassJava");
    }

    @Override
    public String getJarName() {
        return "projects-1.0-SNAPSHOT-jar-with-dependencies.jar";
    }

    @Override
    public String getJavaFolder() {
        return Utils.pathJoin("src", "main", "java");
    }

    @Override
    public String getTargetSource() {
        return Utils.pathJoin("projects");
    }

    @Override
    public String getProjectsJavaFolder() {
        return Utils.pathJoin("projects", getJavaFolder(), "IntroClassJava");
    }

    @Override
    public String getPomPath() {
        return Utils.pathJoin(getTargetSource(), "pom.xml");
    }

    @Override
    public String getJarPath() {
        return Utils.pathJoin(getTargetSource(), "target", getJarName());
    }

    @Override
    public String getSeedFileInputsFolder() {
        return Utils.pathJoin("projects", "src", "main", "resources", "introclass_test_files");
    }

}
