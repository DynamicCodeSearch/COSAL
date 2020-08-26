public String next() {
    if (!hasNext())
        throw new NoSuchElementException();
    StringBuilder sb = new StringBuilder();
    int b = readByte();
    while (!isSpaceChar(b)) {
        sb.appendCodePoint(b);
        b = readByte();
    }
    return sb.toString();
}