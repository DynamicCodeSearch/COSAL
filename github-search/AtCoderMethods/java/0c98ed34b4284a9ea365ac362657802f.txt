private static void insertionSort(IntList list, int from, int to, IntComparator comparator) {
    for (int i = from + 1; i <= to; i++) {
        int value = list.get(i);
        for (int j = i - 1; j >= from; j--) {
            if (comparator.compare(list.get(j), value) <= 0) {
                break;
            }
            list.swap(j, j + 1);
        }
    }
}