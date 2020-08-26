public int readSkipSpace() {
    int c;
    do {
        c = read();
    } while (isSpace(c));
    return c;
}