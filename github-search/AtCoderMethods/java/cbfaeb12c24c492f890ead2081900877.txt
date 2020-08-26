long[] nextLongArray(int n) {
    long[] arr = new long[n];
    int i = 0;
    while (i < n) {
        arr[i++] = nextLong();
    }
    return arr;
}