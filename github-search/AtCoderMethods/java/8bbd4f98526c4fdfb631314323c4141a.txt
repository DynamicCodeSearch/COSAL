public void print(long[] array) {
    for (int i = 0; i < array.length; i++) {
        if (i != 0) {
            writer.print(' ');
        }
        writer.print(array[i]);
    }
}