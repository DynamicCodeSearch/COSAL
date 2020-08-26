public int read() {
    if (snumChars == -1)
        throw new InputMismatchException();
    if (curChar >= snumChars) {
        curChar = 0;
        try {
            snumChars = stream.read(buf);
        } catch (IOException e) {
            throw new InputMismatchException();
        }
        if (snumChars <= 0)
            return -1;
    }
    return buf[curChar++];
}