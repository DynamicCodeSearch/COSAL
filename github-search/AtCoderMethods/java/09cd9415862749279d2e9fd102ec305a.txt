public boolean union(int x, int y) {
    x = root(x);
    y = root(y);
    if (x != y) {
        if (parent[y] < parent[x]) {
            int tmp = y;
            y = x;
            x = tmp;
        }
        parent[x] += parent[y];
        parent[y] = x;
        return true;
    }
    return false;
}