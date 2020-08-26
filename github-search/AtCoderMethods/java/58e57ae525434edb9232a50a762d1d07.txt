int sum(int begin, int end) {
    if (begin == 0)
        return sum(end);
    return sum(end) - sum(begin - 1);
}