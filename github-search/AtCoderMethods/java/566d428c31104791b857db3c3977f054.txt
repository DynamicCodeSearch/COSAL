public static int[][] parentToG(int[] par) {
    int n = par.length;
    int[] ct = new int[n];
    for (int i = 0; i < n; i++) {
        if (par[i] >= 0) {
            ct[i]++;
            ct[par[i]]++;
        }
    }
    int[][] g = new int[n][];
    for (int i = 0; i < n; i++) {
        g[i] = new int[ct[i]];
    }
    for (int i = 0; i < n; i++) {
        if (par[i] >= 0) {
            g[par[i]][--ct[par[i]]] = i;
            g[i][--ct[i]] = par[i];
        }
    }
    return g;
}