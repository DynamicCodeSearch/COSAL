public final boolean flag(int id, int bit) {
    return (flags[id] >> bit & 1) != 0;
}