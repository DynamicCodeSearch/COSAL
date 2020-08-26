private byte read() throws IOException {
    if (bufferPointer == bytesRead)
        fillBuffer();
    return buffer[bufferPointer++];
}