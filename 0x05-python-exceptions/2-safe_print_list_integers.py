#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for item in my_list:
            if type(item) is int:
                print("{:d}".format(item), end=' ')
                count += 1

            if count == x:
                break
    except TypeError:
        pass

    print()
    return count
