void addEdge(int v, int w) {
    adj[v].add(w);
    adj[w].add(v);
}