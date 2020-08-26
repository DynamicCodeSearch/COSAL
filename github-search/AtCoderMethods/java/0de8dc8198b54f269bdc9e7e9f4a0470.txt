public String readString() {
    int c = read();
    while (isSpaceChar(c)) {
        c = read();
    }
    StringBuilder res = new StringBuilder();
    do {
        res.appendCodePoint(c);
        c = read();
    } while (!isSpaceChar(c));
    return res.toString();
}