private String peekToken() {
    if (token == null)
        try {
            while (st == null || !st.hasMoreTokens()) {
                line = r.readLine();
                if (line == null)
                    return null;
                st = new StringTokenizer(line);
            }
            token = st.nextToken();
        } catch (IOException e) {
        }
    return token;
}