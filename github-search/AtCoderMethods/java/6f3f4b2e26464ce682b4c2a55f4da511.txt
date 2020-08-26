public boolean hasNext() {
    skip();
    return hasNextByte();
}