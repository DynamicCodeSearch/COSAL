boolean hasMoreTokens() {
    while (st == null || !st.hasMoreTokens()) {
        String s = null;
        try {
            s = br.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        if (s == null)
            return false;
        st = new StringTokenizer(s);
    }
    return true;
}