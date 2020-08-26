public static int[] enumLowestPrimeFactors(int n) {
    int tot = 0;
    int[] lpf = new int[n + 1];
    int u = n + 32;
    double lu = Math.log(u);
    int[] primes = new int[(int) (u / lu + u / lu / lu * 1.5)];
    for (int i = 2; i <= n; i++) lpf[i] = i;
    for (int p = 2; p <= n; p++) {
        if (lpf[p] == p)
            primes[tot++] = p;
        int tmp;
        for (int i = 0; i < tot && primes[i] <= lpf[p] && (tmp = primes[i] * p) <= n; i++) {
            lpf[tmp] = primes[i];
        }
    }
    return lpf;
}