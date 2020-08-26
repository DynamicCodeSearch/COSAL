public String readString() {
    int c = snext();
    while (isSpaceChar(c)) {
        c = snext();
    }
    StringBuilder res = new StringBuilder();
    do {
        res.appendCodePoint(c);
        c = snext();
    } while (!isSpaceChar(c));
    return res.toString();
}