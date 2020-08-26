public static int[][][] packWD(int n, int[] from, int[] to, int[] w, int sup) {
    int[][][] g = new int[n][][];
    int[] p = new int[n];
    for (int i = 0; i < sup; i++) p[from[i]]++;
    for (int i = 0; i < n; i++) g[i] = new int[p[i]][2];
    for (int i = 0; i < sup; i++) {
        --p[from[i]];
        g[from[i]][p[from[i]]][0] = to[i];
        g[from[i]][p[from[i]]][1] = w[i];
    }
    return g;
}