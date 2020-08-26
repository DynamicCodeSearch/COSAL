public char nextChar() {
    while (true) {
        final int c = read();
        if (!isSpace[c]) {
            return (char) c;
        }
    }
}