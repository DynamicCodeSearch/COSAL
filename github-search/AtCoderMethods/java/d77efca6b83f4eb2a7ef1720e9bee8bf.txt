public String nextLine() {
    String line = "";
    try {
        line = br.readLine();
    } catch (Exception e) {
        e.printStackTrace();
    }
    return line;
}