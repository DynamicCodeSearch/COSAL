private static void siftDown(IntList list, int start, int end, IntComparator comparator, int delta) {
    int value = list.get(start);
    while (true) {
        int child = ((start - delta) << 1) + 1 + delta;
        if (child > end) {
            return;
        }
        int childValue = list.get(child);
        if (child + 1 <= end) {
            int otherValue = list.get(child + 1);
            if (comparator.compare(otherValue, childValue) > 0) {
                child++;
                childValue = otherValue;
            }
        }
        if (comparator.compare(value, childValue) >= 0) {
            return;
        }
        list.swap(start, child);
        start = child;
    }
}