public static void decreaseByOne(int[]... arrays) {
    for (int[] array : arrays) {
        for (int i = 0; i < array.length; i++) {
            array[i]--;
        }
    }
}