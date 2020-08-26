long[] nextLongArrayOneBased(int n) {
    long[] arr = new long[n + 1];
    int i = 1;
    while (i <= n) {
        arr[i++] = nextLong();
    }
    return arr;
}