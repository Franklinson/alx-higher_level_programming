#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for char in str:
        uppercase_char = chr(ord(char) - 32) if "a" <= char <= "z" else char
        uppercase_str += uppercase_char

    print(uppercase_str, end="\n")
