#!/usr/bin/python3
# a function that finds a peak in a list of unsorted integers.
def find_peak(list_of_integers):
  """Finds the peak element in a list of integers.

  Args:
    list_of_integers: A list of integers.

  Returns:
    The index of the peak element.
  """

  low = 0
  high = len(list_of_integers) - 1

  while low <= high:
    mid = (low + high) // 2

    if list_of_integers[mid - 1] < list_of_integers[mid] and \
        list_of_integers[mid + 1] < list_of_integers[mid]:
      return mid
    elif list_of_integers[mid - 1] > list_of_integers[mid]:
      high = mid - 1
    else:
      low = mid + 1

  return -1
