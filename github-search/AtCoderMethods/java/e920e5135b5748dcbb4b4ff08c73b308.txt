public int addEdge(int fromID, int toID, long weight, long capacity, int reverseEdge) {
    ensureEdgeCapacity(edgeCount + 1);
    if (firstOutbound[fromID] != -1) {
        nextOutbound[edgeCount] = firstOutbound[fromID];
    } else {
        nextOutbound[edgeCount] = -1;
    }
    firstOutbound[fromID] = edgeCount;
    if (firstInbound != null) {
        if (firstInbound[toID] != -1) {
            nextInbound[edgeCount] = firstInbound[toID];
        } else {
            nextInbound[edgeCount] = -1;
        }
        firstInbound[toID] = edgeCount;
    }
    this.from[edgeCount] = fromID;
    this.to[edgeCount] = toID;
    if (capacity != 0) {
        if (this.capacity == null) {
            this.capacity = new long[from.length];
        }
        this.capacity[edgeCount] = capacity;
    }
    if (weight != 0) {
        if (this.weight == null) {
            this.weight = new long[from.length];
        }
        this.weight[edgeCount] = weight;
    }
    if (reverseEdge != -1) {
        if (this.reverseEdge == null) {
            this.reverseEdge = new int[from.length];
            Arrays.fill(this.reverseEdge, 0, edgeCount, -1);
        }
        this.reverseEdge[edgeCount] = reverseEdge;
    }
    if (edges != null) {
        edges[edgeCount] = createEdge(edgeCount);
    }
    return edgeCount++;
}