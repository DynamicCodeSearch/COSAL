public static Node root(Node x) {
    if (x == null)
        return null;
    while (x.parent != null) x = x.parent;
    return x;
}