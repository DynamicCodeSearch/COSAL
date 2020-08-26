package edu.ncsu.config.project;

import edu.ncsu.utils.Utils;

public class GuavaConfig extends BaseProjectConfig{


    @Override
    public String getProjectName() {
        return "guava";
    }

    @Override
    public String getDataset() {
        return "OpenSource";
    }

    @Override
    public String getDatasetFolder() {
        return "subjects";
    }

    @Override
    public String getJarName() {
        return "guava-slacc-HEAD-jre-SNAPSHOT-jar-with-dependencies.jar";
    }

    @Override
    public String getJavaFolder() {
        return Utils.pathJoin("src");
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
