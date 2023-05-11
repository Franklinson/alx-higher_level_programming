#!/usr/bin/python3
output = ""

for ascii_code in range(ord('a'), ord('z') + 1):
    output += "{}".format(chr(ascii_code))

print(output)

