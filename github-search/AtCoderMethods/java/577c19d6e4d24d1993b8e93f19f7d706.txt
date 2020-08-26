void run() throws Exception {
    is = INPUT.isEmpty() ? System.in : new ByteArrayInputStream(INPUT.getBytes());
    out = new PrintWriter(System.out);
    long s = System.currentTimeMillis();
    solve();
    out.flush();
    if (!INPUT.isEmpty())
        tr(System.currentTimeMillis() - s + "ms");
}