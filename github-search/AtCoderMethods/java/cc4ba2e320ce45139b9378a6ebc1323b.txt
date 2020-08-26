private int nextPrintable() {
    try {
        int ch;
        while (!isPrintable(ch = br.read())) {
            if (ch == -1) {
                throw new NoSuchElementException();
            }
        }
        return ch;
    } catch (IOException e) {
        throw new NoSuchElementException();
    }
}