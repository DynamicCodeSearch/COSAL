static long gcd(long a, long b) {
    if (a % b == 0)
        return b;
    return gcd(b, a % b);
}