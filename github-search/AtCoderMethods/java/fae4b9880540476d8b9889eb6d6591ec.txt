private int readByte() {
    if (hasNextByte())
        return buffer[curbuf++];
    else
        return -1;
}