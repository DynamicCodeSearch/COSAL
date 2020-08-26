public static BCDatum decomposeToBiconnectedComponents(int[][][] g) {
    int n = g.length;
    int m = 0;
    for (int[][] row : g) m += row.length;
    m /= 2;
    BCDatum d = new BCDatum();
    d.g = g;
    d.gen = 0;
    d.low = new int[n];
    Arrays.fill(d.low, -1);
    d.ord = new int[n];
    Arrays.fill(d.ord, -1);
    d.edgeStack = new int[m];
    d.esp = 0;
    d.edgeClus = new int[m];
    Arrays.fill(d.edgeClus, -1);
    d.visited = new boolean[n];
    d.parente = new int[n];
    d.isArtic = new boolean[n];
    Arrays.fill(d.parente, -1);
    for (int i = 0; i < n; i++) {
        if (!d.visited[i])
            dfsBC(i, d);
    }
    assert d.esp == 0;
    return d;
}