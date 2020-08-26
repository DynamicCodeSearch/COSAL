String nextLine() {
    String s = null;
    try {
        s = reader.readLine();
    } catch (IOException e) {
        e.printStackTrace();
    }
    return s;
}