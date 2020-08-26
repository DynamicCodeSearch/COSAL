public int nextInt() {
    int c = pread();
    while (isSpaceChar(c)) c = pread();
    int sgn = 1;
    if (c == '-') {
        sgn = -1;
        c = pread();
    }
    int res = 0;
    do {
        if (c == ',') {
            c = pread();
        }
        if (c < '0' || c > '9') {
            throw new InputMismatchException();
        }
        res *= 10;
        res += c - '0';
        c = pread();
    } while (!isSpaceChar(c));
    return res * sgn;
}