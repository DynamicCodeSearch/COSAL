package edu.ncsu.config;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class CodeSeerProperties {

    private static Properties PROPERTIES = null;

    private static String PROP_FILE_NAME = "config.properties";

    public static String getProperties(String name) {
        if (PROPERTIES == null) {
            PROPERTIES = new Properties();
            try {
                InputStream inputStream = CodeSeerProperties.class.getClassLoader().getResourceAsStream(PROP_FILE_NAME);
                PROPERTIES.load(inputStream);
            } catch (IOException ignored) {
                throw new RuntimeException(String.format("@COSAL: Property file '%s' not found in classpath", name));
            }
        }
        return PROPERTIES.getProperty(name);
    }

}
