int reads(int len, boolean[] accept) {
    try {
        while (true) {
            final int c = read();
            if (accept[c]) {
                break;
            }
            if (str.length == len) {
                char[] rep = new char[str.length * 3 / 2];
                System.arraycopy(str, 0, rep, 0, str.length);
                str = rep;
            }
            str[len++] = (char) c;
        }
    } catch (MyInput.EndOfFileRuntimeException e) {
    }
    return len;
}