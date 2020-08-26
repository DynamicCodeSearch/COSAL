public long[] nextLongArray(int n) {
    long[] arr = new long[n];
    for (int i = 0; i < n; i++) {
        arr[i] = nextLong();
    }
    return arr;
}