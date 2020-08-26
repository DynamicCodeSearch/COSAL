public int read() {
    if (pos >= readLen) {
        pos = 0;
        try {
            readLen = in.read(buffer);
        } catch (IOException e) {
            throw new RuntimeException();
        }
        if (readLen <= 0) {
            throw new MyInput.EndOfFileRuntimeException();
        }
    }
    return buffer[pos++];
}