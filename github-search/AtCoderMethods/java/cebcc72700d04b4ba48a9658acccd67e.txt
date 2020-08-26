void dfsTarjan(int v) {
    vis[v] = globalTime;
    low[v] = globalTime;
    ++globalTime;
    stack[sp++] = v;
    onStack[v] = true;
    for (int e = firstEdge[v]; e >= 0; e = edgeNxt[e]) {
        int u = edgeDst[e];
        if (vis[u] < 0) {
            dfsTarjan(u);
            if (low[v] > low[u]) {
                low[v] = low[u];
            }
        } else if (onStack[u] && low[v] > vis[u]) {
            low[v] = vis[u];
        }
    }
    if (low[v] == vis[v]) {
        while (true) {
            int u = stack[--sp];
            onStack[u] = false;
            comp[u] = numComps;
            if (u == v) {
                break;
            }
        }
        ++numComps;
    }
}