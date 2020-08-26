public long nextLong() {
    if (!hasNext())
        throw new NoSuchElementException();
    int c = readByte();
    while (isSpaceChar(c)) c = readByte();
    boolean minus = false;
    if (c == '-') {
        minus = true;
        c = readByte();
    }
    long res = 0;
    do {
        if (c < '0' || c > '9')
            throw new InputMismatchException();
        res = res * 10 + c - '0';
        c = readByte();
    } while (!isSpaceChar(c));
    return (minus) ? -res : res;
}