static int rand(int l, int r) {
    return l + rng.nextInt(r - l + 1);
}