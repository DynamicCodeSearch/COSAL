public final int addFlowWeightedEdge(int from, int to, long weight, long capacity) {
    if (capacity == 0) {
        return addEdge(from, to, weight, 0, -1);
    } else {
        int lastEdgeCount = edgeCount;
        addEdge(to, from, -weight, 0, lastEdgeCount + entriesPerEdge());
        return addEdge(from, to, weight, capacity, lastEdgeCount);
    }
}