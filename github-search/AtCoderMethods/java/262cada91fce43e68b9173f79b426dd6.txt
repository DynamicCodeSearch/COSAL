public char[][] nextCharMap(int n, int m) {
    char[][] map = new char[n][m];
    for (int i = 0; i < n; i++) map[i] = next().toCharArray();
    return map;
}