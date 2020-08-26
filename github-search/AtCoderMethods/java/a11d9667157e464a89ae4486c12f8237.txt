private String nextToken() {
    String ans = peekToken();
    token = null;
    return ans;
}