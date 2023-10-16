t = int(input())


def find_min_steps(n: int, a):
    idx_first = -1
    for i in range(0, n):
        if a[i]:
            idx_first = i
            break

    idx_last = n
    for i in range(n - 1, -1, -1):
        if a[i]:
            idx_last = i
            break

    count_zeros = 0
    for i in range(idx_first + 1, idx_last):
        if a[i] == 0:
            count_zeros += 1

    return count_zeros


while t:
    n = int(input())
    a = [int(i) for i in input().split(' ')]
    print(find_min_steps(n, a))

    t -= 1
