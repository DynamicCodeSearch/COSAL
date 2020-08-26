public void close() throws IOException {
    if (din == null)
        return;
    din.close();
}