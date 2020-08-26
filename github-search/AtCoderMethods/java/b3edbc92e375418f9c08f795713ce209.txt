public double readDouble() {
    int c = read();
    while (isSpaceChar(c)) {
        c = read();
    }
    int sgn = 1;
    if (c == '-') {
        sgn = -1;
        c = read();
    }
    double res = 0;
    while (!isSpaceChar(c) && c != '.') {
        if (c == 'e' || c == 'E') {
            return res * Math.pow(10, readInt());
        }
        if (c < '0' || c > '9') {
            throw new InputMismatchException();
        }
        res *= 10;
        res += c - '0';
        c = read();
    }
    if (c == '.') {
        c = read();
        double m = 1;
        while (!isSpaceChar(c)) {
            if (c == 'e' || c == 'E') {
                return res * Math.pow(10, readInt());
            }
            if (c < '0' || c > '9') {
                throw new InputMismatchException();
            }
            m /= 10;
            res += (c - '0') * m;
            c = read();
        }
    }
    return res * sgn;
}