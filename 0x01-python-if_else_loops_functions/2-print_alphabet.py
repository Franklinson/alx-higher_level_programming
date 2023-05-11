#!/usr/bin/python3
start_ascii = ord('a')
end_ascii = ord('z')

for ascii_code in range(start_ascii, end_ascii + 1):
    print(chr(ascii_code), end='')

print()
