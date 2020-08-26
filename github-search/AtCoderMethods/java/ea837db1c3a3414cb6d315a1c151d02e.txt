public static int[] sort(int[] array, int from, int to, IntComparator comparator) {
    if (from == 0 && to == array.length) {
        new IntArray(array).sort(comparator);
    } else {
        new IntArray(array).subList(from, to).sort(comparator);
    }
    return array;
}