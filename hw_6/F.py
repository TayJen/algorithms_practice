import sys

N, K = map(int, input().split(' '))
arr = [0] * (N + 1)
t = [0] * (N + 1)


def prefix_sum(i: int) -> int:
    res = 0
    while i >= 0:
        res += t[i]
        i = (i & (i + 1)) - 1
    return res


def range_sum(l: int, r: int) -> int:
    return prefix_sum(r) - prefix_sum(l-1)


def update(i: int, delta: int):
    while i <= N:
        t[i] += delta
        i = i | (i + 1)


for _ in range(K):
    line = sys.stdin.readline()
    if line[0] == 'A':
        i, x = map(int, line.split(' ')[1:])
        update(i, x - arr[i])
    elif line[0] == 'Q':
        l, r = map(int, line.split(' ')[1:])
        print(range_sum(l, r))
