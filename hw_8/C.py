from typing import List


def find_solution(n: int, arr_1: List[int], m: int, arr_2: List[int]):
    size = max(n, m) + 5
    arr_1 = [0] + arr_1 + [0] * (size - n)
    arr_2 = [0] + arr_2 + [0] * (size - m)
    f, pre = [], []
    for _ in range(size):
        f.append([0] * size)
        pre.append([0] * size)

    for i in range(1, n+1):
        fmax = 0
        pos = 0
        for j in range(1, m+1):
            f[i][j], pre[i][j] = f[i-1][j], pre[i-1][j]
            if arr_1[i] == arr_2[j]:
                if f[i][j] < fmax + 1:
                    f[i][j] = fmax + 1
                    pre[i][j] = pos
            if arr_1[i] > arr_2[j]:
                if f[i-1][j] > fmax:
                    fmax = f[i-1][j]
                    pos = j

    res = last = tot = 0
    path = [0] * size

    for j in range(1, m+1):
        if res < f[n][j]:
            res = f[n][j]
            last = j

    print(res)

    i, j = n, last
    while i or j:
        if pre[i][j] != j:
            tot += 1
            path[tot] = arr_2[j]
        j = pre[i][j]
        i -= 1

    while tot:
        print(path[tot], end=' ')
        tot -= 1


def main():
    n = int(input())
    arr_1 = [int(i) for i in input().split(' ')]

    m = int(input())
    arr_2 = [int(i) for i in input().split(' ')]

    find_solution(n, arr_1, m, arr_2)


if __name__ == "__main__":
    main()
