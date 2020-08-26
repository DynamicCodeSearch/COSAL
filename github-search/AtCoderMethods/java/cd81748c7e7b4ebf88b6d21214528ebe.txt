public int peek() {
    if (numChars == -1) {
        return -1;
    }
    if (curChar >= numChars) {
        curChar = 0;
        try {
            numChars = stream.read(buf);
        } catch (IOException e) {
            return -1;
        }
        if (numChars <= 0) {
            return -1;
        }
    }
    return buf[curChar];
}