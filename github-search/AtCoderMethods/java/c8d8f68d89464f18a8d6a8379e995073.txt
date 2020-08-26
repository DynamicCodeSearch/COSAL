public int get(int at) {
    if (at >= size) {
        throw new IndexOutOfBoundsException("at = " + at + ", size = " + size);
    }
    return data[at];
}