String nextToken() throws IOException {
    while (stok == null || !stok.hasMoreTokens()) {
        String s = br.readLine();
        if (s == null) {
            return null;
        }
        stok = new StringTokenizer(s);
    }
    return stok.nextToken();
}