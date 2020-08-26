private static void heapSort(IntList list, int from, int to, IntComparator comparator) {
    for (int i = (to + from - 1) >> 1; i >= from; i--) {
        siftDown(list, i, to, comparator, from);
    }
    for (int i = to; i > from; i--) {
        list.swap(from, i);
        siftDown(list, from, i - 1, comparator, from);
    }
}