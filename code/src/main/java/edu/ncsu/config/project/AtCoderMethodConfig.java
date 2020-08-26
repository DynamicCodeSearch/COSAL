package edu.ncsu.config.project;

import edu.ncsu.utils.Utils;

public class AtCoderMethodConfig extends BaseProjectConfig{

    public String getProjectName() {
        return "atcoder";
    }

    public String getDataset() {
        return "AtCoderMethods";
    }

    @Override
    public String getDatasetFolder() {
        return "subjects";
    }

    @Override
    public String getJarName() {
        return "atcoder-1.0-SNAPSHOT-jar-with-dependencies.jar";
    }

    @Override
    public String getJavaFolder() {
        return Utils.pathJoin("src", "main", "java");
    }

    @Override
    public String getTargetSource() {
        return Utils.pathJoin("subjects", getProjectName());
    }

    @Override
    public String getProjectsJavaFolder() {
        return Utils.pathJoin("subjects", getProjectName(), getJavaFolder());
    }

    @Override
    public String getPomPath() {
        return Utils.pathJoin(getTargetSource(), "pom.xml");
    }

    @Override
    public String getJarPath() {
        return Utils.pathJoin(getTargetSource(), "target", getJarName());
    }

}
