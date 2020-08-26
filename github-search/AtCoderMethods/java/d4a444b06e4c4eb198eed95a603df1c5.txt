public long[] nextSumLongArray(int n) {
    long[] array = new long[n];
    array[0] = nextInt();
    for (int i = 1; i < n; ++i) array[i] = array[i - 1] + nextInt();
    return array;
}