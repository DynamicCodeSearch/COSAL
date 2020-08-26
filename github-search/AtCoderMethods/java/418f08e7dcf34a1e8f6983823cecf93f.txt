public String nextLine() {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = "";
    try {
        str = br.readLine();
    } catch (IOException e) {
        e.printStackTrace();
    }
    return str;
}