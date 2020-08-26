public static Node disconnect(Node a) {
    if (a == null)
        return null;
    a.left = a.right = a.parent = null;
    return update(a);
}