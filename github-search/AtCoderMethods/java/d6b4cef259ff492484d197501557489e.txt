public void removeAt(int index) {
    if (index >= size || index < 0) {
        throw new IndexOutOfBoundsException("at = " + index + ", size = " + size);
    }
    if (index != size - 1) {
        System.arraycopy(data, index + 1, data, index, size - index - 1);
    }
    size--;
}