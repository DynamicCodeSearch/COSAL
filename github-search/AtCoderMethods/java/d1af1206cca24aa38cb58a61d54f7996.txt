private int scan() {
    if (index >= total) {
        index = 0;
        try {
            total = in.read(buf);
        } catch (Exception e) {
            e.printStackTrace();
        }
        if (total <= 0)
            return -1;
    }
    return buf[index++];
}