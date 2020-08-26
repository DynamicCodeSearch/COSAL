public int nextInt() {
    int c = read();
    while (isSpaceChar(c)) {
        c = read();
    }
    int sgn = 1;
    if (c == '-') {
        sgn = -1;
        c = read();
    }
    int res = 0;
    do {
        res *= 10;
        res += c - '0';
        c = read();
    } while (!isSpaceChar(c));
    return res * sgn;
}