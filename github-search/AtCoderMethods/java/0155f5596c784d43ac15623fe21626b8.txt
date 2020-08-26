public String nextToken() throws IOException {
    while (in == null || !in.hasMoreTokens()) {
        in = new StringTokenizer(br.readLine());
    }
    return in.nextToken();
}