public int root(int x) {
    return parent[x] < 0 ? x : (parent[x] = root(parent[x]));
}