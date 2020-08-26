public int read() {
    if (numChars == -1)
        throw new UnknownError();
    if (curChar >= numChars) {
        curChar = 0;
        try {
            numChars = stream.read(buf);
        } catch (IOException e) {
            throw new UnknownError();
        }
        if (numChars <= 0)
            return -1;
    }
    return buf[curChar++];
}