public static void sort(IntList list, IntComparator comparator) {
    quickSort(list, 0, list.size() - 1, (Integer.bitCount(Integer.highestOneBit(list.size()) - 1) * 5) >> 1, comparator);
}