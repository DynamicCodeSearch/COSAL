public long nextLong() throws IOException {
    long ret = 0;
    byte c = read();
    while (c <= ' ') c = read();
    boolean neg = (c == '-');
    if (neg)
        c = read();
    do {
        ret = ret * 10 + c - '0';
    } while ((c = read()) >= '0' && c <= '9');
    if (neg)
        return -ret;
    return ret;
}