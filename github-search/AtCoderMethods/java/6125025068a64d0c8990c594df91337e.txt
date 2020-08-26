public boolean hasNextByte() {
    if (curbuf >= lenbuf) {
        curbuf = 0;
        try {
            lenbuf = in.read(buffer);
        } catch (IOException e) {
            throw new InputMismatchException();
        }
        if (lenbuf <= 0)
            return false;
    }
    return true;
}