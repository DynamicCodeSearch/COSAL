protected void ensureEdgeCapacity(int size) {
    if (from.length < size) {
        int newSize = Math.max(size, 2 * from.length);
        if (edges != null) {
            edges = resize(edges, newSize);
        }
        from = resize(from, newSize);
        to = resize(to, newSize);
        nextOutbound = resize(nextOutbound, newSize);
        if (nextInbound != null) {
            nextInbound = resize(nextInbound, newSize);
        }
        if (weight != null) {
            weight = resize(weight, newSize);
        }
        if (capacity != null) {
            capacity = resize(capacity, newSize);
        }
        if (reverseEdge != null) {
            reverseEdge = resize(reverseEdge, newSize);
        }
        flags = resize(flags, newSize);
    }
}