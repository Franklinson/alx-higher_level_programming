#!/usr/bin/python3
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - 32 * i)), end="")
    i = 1 - i
