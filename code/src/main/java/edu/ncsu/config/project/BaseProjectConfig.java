package edu.ncsu.config.project;

import org.apache.commons.lang3.NotImplementedException;

public abstract class BaseProjectConfig {

    public String getProjectName() {
        throw new NotImplementedException("Not implemented in baseclass");
    }

    public String getDataset() {
        throw new NotImplementedException("Not implemented in baseclass");
    }

    public String getDatasetFolder() {
        throw new NotImplementedException("Not implemented in baseclass");
    }

    public String getJarName() {
        throw new NotImplementedException("Not implemented in baseclass");
    }

    public String getJavaFolder() {
        throw new NotImplementedException("Not implemented in baseclass");
    }

    public String getTargetSource() {
        throw new NotImplementedException("Not implemented in baseclass");
    }

    public String getProjectsJavaFolder() {
        throw new NotImplementedException("Not implemented in baseclass");
    }

    public String getPomPath() {
        throw new NotImplementedException("Not implemented in baseclass");
    }

    public String getJarPath() {
        throw new NotImplementedException("Not implemented in baseclass");
    }

    public String getSeedFileInputsFolder() {
        throw new NotImplementedException("Not implemented in baseclass");

    }
}
