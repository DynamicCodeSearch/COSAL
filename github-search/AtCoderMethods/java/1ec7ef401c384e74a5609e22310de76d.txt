public String next() {
    while (st == null || !st.hasMoreTokens()) {
        try {
            String rl = in.readLine();
            if (rl == null) {
                return null;
            }
            st = new StringTokenizer(rl);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    return st.nextToken();
}