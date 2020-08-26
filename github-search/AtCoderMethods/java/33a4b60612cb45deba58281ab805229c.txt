public int scanInt() {
    int integer = 0;
    int n = scan();
    while (isWhiteSpace(n)) n = scan();
    int neg = 1;
    if (n == '-') {
        neg = -1;
        n = scan();
    }
    while (!isWhiteSpace(n)) {
        if (n >= '0' && n <= '9') {
            integer *= 10;
            integer += n - '0';
            n = scan();
        }
    }
    return neg * integer;
}