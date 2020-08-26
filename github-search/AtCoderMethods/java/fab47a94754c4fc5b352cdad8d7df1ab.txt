public void addAt(int index, int value) {
    ensureCapacity(size + 1);
    if (index > size || index < 0) {
        throw new IndexOutOfBoundsException("at = " + index + ", size = " + size);
    }
    if (index != size) {
        System.arraycopy(data, index, data, index + 1, size - index);
    }
    data[index] = value;
    size++;
}