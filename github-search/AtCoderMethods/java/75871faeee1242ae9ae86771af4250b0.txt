String nextLine() {
    try {
        int ch;
        while (isCRLF(ch = br.read())) {
            if (ch == -1) {
                throw new NoSuchElementException();
            }
        }
        StringBuilder sb = new StringBuilder();
        do {
            sb.appendCodePoint(ch);
        } while (!isCRLF(ch = br.read()));
        return sb.toString();
    } catch (IOException e) {
        throw new NoSuchElementException();
    }
}