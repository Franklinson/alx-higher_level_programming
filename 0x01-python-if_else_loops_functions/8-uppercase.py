#!/usr/bin/python
def uppercase(str):
    uppercase_str = ""
    for char in str:
        uppercase_char = chr(ord(char) & ~32) if "a" <= char <= "z" else char
        uppercase_str += uppercase_char

    print("{}\n".format(uppercase_str))
