public long[] nextLongArray(int n) {
    long[] res = new long[n];
    for (int i = 0; i < n; i++) {
        res[i] = nextLong();
    }
    return res;
}