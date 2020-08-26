public static int[][][] packWU(int n, int[] from, int[] to, int[] w) {
    int[][][] g = new int[n][][];
    int[] p = new int[n];
    for (int f : from) p[f]++;
    for (int t : to) p[t]++;
    for (int i = 0; i < n; i++) g[i] = new int[p[i]][2];
    for (int i = 0; i < from.length; i++) {
        --p[from[i]];
        g[from[i]][p[from[i]]][0] = to[i];
        g[from[i]][p[from[i]]][1] = w[i];
        --p[to[i]];
        g[to[i]][p[to[i]]][0] = from[i];
        g[to[i]][p[to[i]]][1] = w[i];
    }
    return g;
}