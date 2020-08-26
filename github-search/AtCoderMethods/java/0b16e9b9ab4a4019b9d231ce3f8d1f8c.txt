private void ensureCapacity(int capacity) {
    if (data.length >= capacity) {
        return;
    }
    capacity = Math.max(2 * data.length, capacity);
    data = Arrays.copyOf(data, capacity);
}