package edu.ncsu.utils;

import edu.ncsu.config.ProjectConfig;
import edu.ncsu.config.Settings;
import org.apache.commons.io.FileUtils;
import org.apache.maven.shared.invoker.*;

import java.io.File;
import java.io.IOException;
import java.util.Arrays;
import java.util.logging.Logger;

public class MavenUtils {

    private final static Logger LOGGER = Logger.getLogger(MavenUtils.class.getName());

    private static String getMavenHome() {
        String mavenHome = System.getProperty("maven.home");
        if (mavenHome == null)
            mavenHome = System.getenv("M2_HOME");
        if (mavenHome == null)
            throw new RuntimeException("@COSAL: Cannot find maven home. Configure the environment variable 'M2_HOME'");
        return mavenHome;
    }

    public static void buildProject() {
        LOGGER.info(String.format("Building jar for project '%s' ... ", ProjectConfig.PROJECT_NAME));
        InvocationRequest request = new DefaultInvocationRequest();
        request.setPomFile(new File(ProjectConfig.POM_PATH));
        request.setGoals(Arrays.asList("clean", "install"));
        Invoker invoker = new DefaultInvoker();
        invoker.setMavenHome(new File(getMavenHome()));
        try {
            InvocationResult result =  invoker.execute(request);
            if (result.getExitCode() != 0) {
                throw new RuntimeException(String.format("@COSAL: Build failed for project '%s' !!!", ProjectConfig.PROJECT_NAME));
            }
        } catch (MavenInvocationException e) {
            throw new RuntimeException(e);
        }
        String sourcePath = ProjectConfig.JAR_PATH;
        String targetPath = Settings.PROJECTS_JAR_PATH;
        try {
            FileUtils.copyFile(new File(sourcePath), new File(targetPath));
        } catch (IOException e) {
            LOGGER.severe("Failed to copy generated jar into 'code/jars/' folder ... ");
            throw new RuntimeException(e);
        }
        LOGGER.info("Build Success!");
    }

    public static void main(String[] args) {
//        buildProject();
        System.out.println(getMavenHome());
    }
}
