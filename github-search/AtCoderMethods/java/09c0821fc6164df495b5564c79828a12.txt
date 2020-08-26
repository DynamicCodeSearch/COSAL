public long[] nextLongArray(int n) {
    long[] a = new long[n];
    for (int i = 0; i < n; i++) a[i] = nextLong();
    return a;
}