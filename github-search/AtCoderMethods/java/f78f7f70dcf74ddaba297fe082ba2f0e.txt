public int nextInt() {
    int c = snext();
    while (isSpaceChar(c)) {
        c = snext();
    }
    int sgn = 1;
    if (c == '-') {
        sgn = -1;
        c = snext();
    }
    int res = 0;
    do {
        if (c < '0' || c > '9')
            throw new InputMismatchException();
        res *= 10;
        res += c - '0';
        c = snext();
    } while (!isSpaceChar(c));
    return res * sgn;
}