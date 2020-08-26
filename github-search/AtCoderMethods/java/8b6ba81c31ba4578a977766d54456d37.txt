int[] nextIntArrayOneBased(int n) {
    int[] arr = new int[n + 1];
    int i = 1;
    while (i <= n) {
        arr[i++] = nextInt();
    }
    return arr;
}