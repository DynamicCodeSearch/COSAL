public final int addWeightedEdge(int from, int to, long weight) {
    return addFlowWeightedEdge(from, to, weight, 0);
}