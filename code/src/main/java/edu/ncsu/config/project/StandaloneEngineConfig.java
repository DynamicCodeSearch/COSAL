package edu.ncsu.config.project;

import edu.ncsu.utils.Utils;

public class StandaloneEngineConfig extends BaseProjectConfig {
    @Override
    public String getProjectName() {
        return "Standalone";
    }

    @Override
    public String getDataset() {
        return "Standalone";
    }

    @Override
    public String getDatasetFolder() {
        return Utils.pathJoin("projects", getJavaFolder(), "Standalone");
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
        return Utils.pathJoin("projects", getJavaFolder(), "Standalone");
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
