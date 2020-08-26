public boolean isSpaceChar(int c) {
    if (filter != null)
        return filter.isSpaceChar(c);
    return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
}