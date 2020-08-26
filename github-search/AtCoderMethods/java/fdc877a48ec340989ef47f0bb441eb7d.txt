public void set(int index, int value) {
    if (index >= size) {
        throw new IndexOutOfBoundsException("at = " + index + ", size = " + size);
    }
    data[index] = value;
}