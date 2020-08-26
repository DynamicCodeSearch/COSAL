public String nextString() {
    int c = read();
    while (isSpaceChar(c)) {
        c = read();
    }
    StringBuilder res = new StringBuilder();
    do {
        if (Character.isValidCodePoint(c)) {
            res.appendCodePoint(c);
        }
        c = read();
    } while (!isSpaceChar(c));
    return res.toString();
}