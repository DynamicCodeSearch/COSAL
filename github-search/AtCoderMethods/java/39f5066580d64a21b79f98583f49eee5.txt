public long[] nextLongArray(int n) {
    long[] array = new long[n];
    for (int i = 0; i < n; i++) array[i] = nextLong();
    return array;
}