public String next() throws IOException {
    while (st == null || !st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
    return st.nextToken();
}