#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Type Exception")
    except TypeError as e:
        raise e
