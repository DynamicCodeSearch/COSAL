public int nextInt() {
    int sgn = 1;
    int c = readSkipSpace();
    if (c == '-') {
        sgn = -1;
        c = read();
    }
    int res = 0;
    do {
        if (c < '0' || c > '9') {
            throw new InputMismatchException();
        }
        res = res * 10 + c - '0';
        c = read();
    } while (!isSpace(c));
    res *= sgn;
    return res;
}