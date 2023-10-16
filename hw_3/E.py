import sys


n, k = [int(i) for i in input().split()]
raw_input = sys.stdin.readlines()
rope_lengths = [int(val) for val in raw_input]


def find_summ_arr_divided_by_x(arr, x):
    summ = 0
    for val in arr:
        summ += val // x
    return summ


def find_shortest_rope(rope_lengths, num_ropes):
    if find_summ_arr_divided_by_x(rope_lengths, 1) < num_ropes:
        return 0

    l, r = 1, max(rope_lengths) + 1
    for _ in range(50):
        mid = (l + r) // 2
        summ = find_summ_arr_divided_by_x(rope_lengths, mid)
        if summ >= num_ropes:
            l = mid
        else:
            r = mid

    return mid


print(find_shortest_rope(rope_lengths, k))
