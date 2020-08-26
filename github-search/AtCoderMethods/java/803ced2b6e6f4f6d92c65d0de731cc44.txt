public int hashCode() {
    return new Long(x).hashCode() * 31 + new Long(y).hashCode();
}