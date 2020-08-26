public String next() {
    while (st == null || !st.hasMoreTokens()) {
        try {
            st = new StringTokenizer(in.readLine());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    return st.nextToken();
}