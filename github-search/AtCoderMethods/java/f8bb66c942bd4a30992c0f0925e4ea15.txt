void close() {
    try {
        reader.close();
    } catch (IOException e) {
        e.printStackTrace();
    }
}