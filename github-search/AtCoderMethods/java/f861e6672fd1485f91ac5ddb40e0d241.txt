private int readByte() {
    if (hasNextByte())
        return buffer[ptr++];
    else
        return -1;
}