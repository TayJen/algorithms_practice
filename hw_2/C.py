# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[0]

#     less = []
#     equal = []
#     greater = []

#     for elem in arr:
#         if elem < pivot:
#             less.append(elem)
#         elif elem == pivot:
#             equal.append(elem)
#         else:
#             greater.append(elem)

#     return quicksort(less) + equal + quicksort(greater)
# Memory bad

import random


def quicksort(arr, left: int, right: int):
    """
    Sort the array xs[fst, lst] in-place with vanilla QuickSort

    :param arr:  the list of numbers to sort
    :param left: the first index from arr to begin sorting from,
                 must be in the range [0, len(arr))
    :param right: the last index from arr to stop sorting at
                  must be in the range [left, len(arr))
    :return:    nothing, the side effect is that arr[left, right] is sorted
    """
    if left >= right:
        return

    i, j = left, right
    pivot = arr[random.randint(left, right)]

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1
    quicksort(arr, left, j)
    quicksort(arr, i, right)


n = int(input())
arr = [int(i) for i in input().split(' ')]
quicksort(arr, 0, len(arr)-1)
print(' '.join([str(i) for i in arr]))