package edu.ncsu.mos.blocks;

import com.google.gson.JsonObject;

public class ContestMeta {

    public long submissionId = 0L;

    public String contestType;

    public long contestId = 0L;

    public long problemId = 0L;

    public long execTime = 0L;

    public long codeSize = 0L;

    public long getSubmissionId() {
        return submissionId;
    }

    public void setSubmissionId(long submissionId) {
        this.submissionId = submissionId;
    }

    public String getContestType() {
        return contestType;
    }

    public void setContestType(String contestType) {
        this.contestType = contestType;
    }

    public long getContestId() {
        return contestId;
    }

    public void setContestId(long contestId) {
        this.contestId = contestId;
    }

    public long getProblemId() {
        return problemId;
    }

    public void setProblemId(long problemId) {
        this.problemId = problemId;
    }

    public long getExecTime() {
        return execTime;
    }

    public void setExecTime(long execTime) {
        this.execTime = execTime;
    }

    public long getCodeSize() {
        return codeSize;
    }

    public void setCodeSize(long codeSize) {
        this.codeSize = codeSize;
    }

    public JsonObject toJson() {
        JsonObject json = new JsonObject();
        json.addProperty("submissionId", this.submissionId);
        json.addProperty("contestType", this.contestType);
        json.addProperty("contestId", this.contestId);
        json.addProperty("problemId", this.problemId);
        json.addProperty("execTime", this.execTime);
        json.addProperty("codeSize", this.codeSize);
        return json;
    }

    public static ContestMeta fromJson(JsonObject json) {
        ContestMeta contestMeta =  new ContestMeta();
        if (json.has("submissionId"))
            contestMeta.setSubmissionId(json.get("submissionId").getAsLong());
        if (json.has("contestType"))
            contestMeta.setContestType(json.get("contestType").getAsString());
        if (json.has("contestId"))
            contestMeta.setContestId(json.get("contestId").getAsLong());
        if (json.has("problemId"))
            contestMeta.setProblemId(json.get("problemId").getAsLong());
        if (json.has("execTime"))
            contestMeta.setExecTime(json.get("execTime").getAsLong());
        if (json.has("codeSize"))
            contestMeta.setCodeSize(json.get("codeSize").getAsLong());
        return contestMeta;
    }

    public String makeKey() {
        return String.format("C:%d-P%d", this.contestId, this.problemId);
    }
}
