public boolean hasNext() {
    skipUnprintable();
    return hasNextByte();
}