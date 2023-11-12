import sys

N = int(input())
arr = [[[0] * N for _ in range(N)] for _ in range(N)]


def prefix_sum(x: int, y: int, z: int) -> int:
    res = 0
    x0 = x
    while x0 >= 0:
        y0 = y
        while y0 >= 0:
            z0 = z
            while z0 >= 0:
                res += arr[x0][y0][z0]
                z0 = (z0 & (z0+1)) - 1
            y0 = (y0 & (y0+1)) - 1
        x0 = (x0 & (x0+1)) - 1
    return res


def range_sum(x1, y1, z1, x2, y2, z2) -> int:
    return prefix_sum(x2, y2, z2) - \
        prefix_sum(x1 - 1, y2, z2) - \
        prefix_sum(x2, y1 - 1, z2) - \
        prefix_sum(x2, y2, z1 - 1) + \
        prefix_sum(x1 - 1, y1 - 1, z2) + \
        prefix_sum(x1 - 1, y2, z1 - 1) + \
        prefix_sum(x2, y1 - 1, z1 - 1) - \
        prefix_sum(x1 - 1, y1 - 1, z1 - 1)


def update(x: int, y: int, z: int, delta: int):
    x0 = x
    while x0 < N:
        y0 = y
        while y0 < N:
            z0 = z
            while z0 < N:
                arr[x0][y0][z0] += delta
                z0 = (z0 | (z0+1))
            y0 = (y0 | (y0+1))
        x0 = (x0 | (x0+1))


while True:
    oper = sys.stdin.readline()
    if int(oper[0]) == 1:
        x, y, z, val = map(int, oper.split(' ')[1:])
        update(x, y, z, val)

    elif int(oper[0]) == 2:
        x1, y1, z1, x2, y2, z2 = map(int, oper.split(' ')[1:])
        print(range_sum(x1, y1, z1, x2, y2, z2))

    elif int(oper[0]) == 3:
        break
