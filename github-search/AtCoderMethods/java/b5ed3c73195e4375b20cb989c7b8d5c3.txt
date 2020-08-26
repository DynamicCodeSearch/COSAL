public final int firstOutbound(int vertex) {
    int id = firstOutbound[vertex];
    while (id != -1 && isRemoved(id)) {
        id = nextOutbound[id];
    }
    return id;
}