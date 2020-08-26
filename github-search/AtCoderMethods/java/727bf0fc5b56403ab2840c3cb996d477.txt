public String nextLine() {
    StringBuffer buf = new StringBuffer();
    int c = read();
    while (c != '\n' && c != -1) {
        if (c != '\r')
            buf.appendCodePoint(c);
        c = read();
    }
    return buf.toString();
}