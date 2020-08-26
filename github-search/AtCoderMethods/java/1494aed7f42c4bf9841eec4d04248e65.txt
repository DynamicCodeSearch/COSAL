private void skipUnprintable() {
    while (hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;
}