private static void quickSort(IntList list, int from, int to, int remaining, IntComparator comparator) {
    if (to - from < INSERTION_THRESHOLD) {
        insertionSort(list, from, to, comparator);
        return;
    }
    if (remaining == 0) {
        heapSort(list, from, to, comparator);
        return;
    }
    remaining--;
    int pivotIndex = (from + to) >> 1;
    int pivot = list.get(pivotIndex);
    list.swap(pivotIndex, to);
    int storeIndex = from;
    int equalIndex = to;
    for (int i = from; i < equalIndex; i++) {
        int value = comparator.compare(list.get(i), pivot);
        if (value < 0) {
            list.swap(storeIndex++, i);
        } else if (value == 0) {
            list.swap(--equalIndex, i--);
        }
    }
    quickSort(list, from, storeIndex - 1, remaining, comparator);
    for (int i = equalIndex; i <= to; i++) {
        list.swap(storeIndex++, i);
    }
    quickSort(list, storeIndex, to, remaining, comparator);
}