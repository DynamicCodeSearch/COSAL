public int[] nextIntArray(int n) {
    int[] res = new int[n];
    for (int i = 0; i < n; i++) {
        res[i] = nextInt();
    }
    return res;
}