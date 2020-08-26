public String nextToken() throws Exception {
    while (st == null || !st.hasMoreTokens()) {
        st = new StringTokenizer(in.readLine());
    }
    return st.nextToken();
}