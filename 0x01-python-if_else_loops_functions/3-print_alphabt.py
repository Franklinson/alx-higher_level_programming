#!/usr/bin/python3
for ascii_code in range(ord('a'), ord('z') + 1):
    letter = chr(ascii_code)
    if letter not in ['q', 'e']:
        print("{:s}".format(letter), end='')
