public long readLong() {
    int c = read();
    while (isSpaceChar(c)) {
        c = read();
    }
    int sgn = 1;
    if (c == '-') {
        sgn = -1;
        c = read();
    }
    long res = 0;
    do {
        if (c < '0' || c > '9') {
            throw new InputMismatchException();
        }
        res *= 10;
        res += c - '0';
        c = read();
    } while (!isSpaceChar(c));
    return res * sgn;
}