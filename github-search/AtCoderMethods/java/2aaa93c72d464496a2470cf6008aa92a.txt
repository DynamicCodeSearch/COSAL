void add(int idx, int val) {
    for (int i = idx + 1; i <= n; i += i & (-i)) bit[i - 1] += val;
}