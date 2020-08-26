int[] nextIntArray(int n) {
    int[] arr = new int[n];
    int i = 0;
    while (i < n) {
        arr[i++] = nextInt();
    }
    return arr;
}