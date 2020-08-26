public static int[][] parents3(int[][] g, int root) {
    int n = g.length;
    int[] par = new int[n];
    Arrays.fill(par, -1);
    int[] depth = new int[n];
    depth[0] = 0;
    int[] q = new int[n];
    q[0] = root;
    for (int p = 0, r = 1; p < r; p++) {
        int cur = q[p];
        for (int nex : g[cur]) {
            if (par[cur] != nex) {
                q[r++] = nex;
                par[nex] = cur;
                depth[nex] = depth[cur] + 1;
            }
        }
    }
    return new int[][] { par, q, depth };
}