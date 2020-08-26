private String readLine0() {
    StringBuilder buf = new StringBuilder();
    int c = read();
    while (c != '\n' && c != -1) {
        if (c != '\r') {
            buf.appendCodePoint(c);
        }
        c = read();
    }
    return buf.toString();
}