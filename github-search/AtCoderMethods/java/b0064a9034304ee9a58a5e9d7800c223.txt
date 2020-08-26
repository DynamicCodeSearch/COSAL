public String nextLine() {
    int c = snext();
    while (isSpaceChar(c)) c = snext();
    StringBuilder res = new StringBuilder();
    do {
        res.appendCodePoint(c);
        c = snext();
    } while (!isEndOfLine(c));
    return res.toString();
}