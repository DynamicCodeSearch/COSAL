package edu.ncsu.mos.rest;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import org.apache.http.NameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

public class ASTParser {

    private static String API_URL = "http://127.0.0.1:5000/java/ast";

    private final static Gson GSON = new Gson();

    private final static Logger LOGGER = Logger.getLogger(ASTParser.class.getName());

    public static JsonObject getJavaASTForFunction(String javaCode) {
        try {
            CloseableHttpClient client = HttpClients.createDefault();
            HttpPost httpPost = new HttpPost(API_URL);
            List<NameValuePair> params = new ArrayList<>();
            params.add(new BasicNameValuePair("code", javaCode));
            httpPost.setEntity(new UrlEncodedFormEntity(params));
            CloseableHttpResponse response = client.execute(httpPost);
            JsonObject respObject = GSON.fromJson(EntityUtils.toString(response.getEntity()), JsonObject.class);
            int status = respObject.get("status").getAsInt();
            if (status == 200) {
                return respObject.getAsJsonObject("ast");
            } else {
                LOGGER.severe(String.format("API Error: %s", respObject.get("error_msg").getAsString()));
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return null;
    }

}
