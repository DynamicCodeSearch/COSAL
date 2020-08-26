public double nextDouble() throws IOException {
    double ret = 0, div = 1;
    byte c = read();
    while (c <= ' ') c = read();
    boolean neg = (c == '-');
    if (neg)
        c = read();
    do {
        ret = ret * 10 + c - '0';
    } while ((c = read()) >= '0' && c <= '9');
    if (c == '.') {
        while ((c = read()) >= '0' && c <= '9') {
            ret += (c - '0') / (div *= 10);
        }
    }
    if (neg)
        return -ret;
    return ret;
}