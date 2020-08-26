package edu.ncsu.mains;

import edu.ncsu.arguments.ArgumentGenerator;
import edu.ncsu.arguments.ArgumentMeta;
import edu.ncsu.config.ProjectConfig;
import edu.ncsu.utils.Utils;

import java.util.List;

public class ScratchPad {
    public static void main(String[] args) {
        String seedFilesFolder = ProjectConfig.getSeedFileInputsFolder();
        System.out.println(seedFilesFolder);
        List<String> seedFiles =  Utils.listFilesWithExtension(seedFilesFolder, ".in", true, false, null);
        System.out.println(String.format("Number of seed files: %d", seedFiles.size()));
        System.out.println(ArgumentGenerator.getFileContent(new ArgumentMeta()));
    }
}
