import sys

N, K = [int(i) for i in input().split(' ')]
arr = [0] * (N + 1)


def prefix_sum(i: int) -> int:
    res = 0
    while i > 0:
        res += arr[i]
        i -= i & -i
    return res


def range_sum(l: int, r: int) -> int:
    return prefix_sum(r) - prefix_sum(l-1)


def update(i: int, x: int):
    while i <= N:
        arr[i] += x
        i += i & -i


for oper in sys.stdin.readlines():
    if oper[0] == 'A':
        i, x = map(int, oper.split(' ')[1:])
        update(i, x)
    elif oper[0] == 'Q':
        l, r = map(int, oper.split(' ')[1:])
        print(range_sum(l, r))
