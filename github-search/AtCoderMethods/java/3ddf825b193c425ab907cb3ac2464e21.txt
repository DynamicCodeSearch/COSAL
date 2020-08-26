private void skip() {
    while (hasNextByte() && isSpaceChar(buffer[curbuf])) curbuf++;
}