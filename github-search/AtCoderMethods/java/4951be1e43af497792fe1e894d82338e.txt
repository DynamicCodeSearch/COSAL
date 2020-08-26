public static int index(Node a) {
    if (a == null)
        return -1;
    int ind = count(a.left);
    while (a != null) {
        Node par = a.parent;
        if (par != null && par.right == a) {
            ind += count(par.left) + 1;
        }
        a = par;
    }
    return ind;
}