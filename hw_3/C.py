import sys

n = int(input())

arr = [int(i) for i in input().split()]
arr.sort()

k = int(input())
raw_input = sys.stdin.readlines()


def find_insert_pos_l(value):
    """
        will be inserted the first among the equal elements
        value = arr[insert_pos],
        arr[left_idx] < elem <= arr[right_idx]
    """
    left_idx, right_idx = -1, n
    while abs(right_idx - left_idx) > 1:
        mid_index = (left_idx + right_idx) // 2
        if arr[mid_index] < value:
            left_idx = mid_index
        else:
            right_idx = mid_index
    return left_idx


def find_insert_pos_r(value):
    """
        would be inserted the last among the equal elements
        value = arr[insert_pos],
        arr[left_idx] <= elem < arr[right_idx]
    """
    left_idx, right_idx = -1, n
    while abs(right_idx - left_idx) > 1:
        mid_index = (left_idx + right_idx) // 2
        if arr[mid_index] <= value:
            left_idx = mid_index
        else:
            right_idx = mid_index

    return right_idx


for i in range(k):
    l, r = [int(val) for val in raw_input[i].split(' ')]

    left_idx = find_insert_pos_l(l)
    right_idx = find_insert_pos_r(r)

    # print(right_idx, left_idx)
    print(right_idx - left_idx - 1, end=' ')
    # print()
