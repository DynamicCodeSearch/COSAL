public double[] nextDoubleArray(int n) {
    double[] a = new double[n];
    for (int i = 0; i < n; i++) a[i] = nextDouble();
    return a;
}