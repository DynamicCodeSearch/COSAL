private Edge[] resize(Edge[] array, int size) {
    Edge[] newArray = new Edge[size];
    System.arraycopy(array, 0, newArray, 0, array.length);
    return newArray;
}