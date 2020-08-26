public int nextInt() {
    int len = 0;
    str[len++] = nextChar();
    len = reads(len, isSpace);
    int i = 0;
    int ret = 0;
    if (str[0] == '-') {
        i = 1;
    }
    for (; i < len; i++) ret = ret * 10 + str[i] - '0';
    if (str[0] == '-') {
        ret = -ret;
    }
    return ret;
}