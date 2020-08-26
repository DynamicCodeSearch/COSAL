public final int nextOutbound(int id) {
    id = nextOutbound[id];
    while (id != -1 && isRemoved(id)) {
        id = nextOutbound[id];
    }
    return id;
}