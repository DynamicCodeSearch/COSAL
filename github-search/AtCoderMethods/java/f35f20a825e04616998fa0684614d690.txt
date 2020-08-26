public static Node[] nodes(Node a, Node[] ns, int L, int R) {
    if (a == null)
        return ns;
    nodes(a.left, ns, L, L + count(a.left));
    ns[L + count(a.left)] = a;
    nodes(a.right, ns, R - count(a.right), R);
    return ns;
}