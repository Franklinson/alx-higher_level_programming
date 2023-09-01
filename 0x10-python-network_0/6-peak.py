#!/usr/bin/python3
# a function that finds a peak in a list of unsorted integer.

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of integers to find a peak in.

    Returns:
        int or None: Peak element if found, otherwise None.
    """
    size = len(list_of_integers)

    if size == 0:
        return None

    left = 0
    right = size - 1

    while left < right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
