t = int(input())

while t:
    n, k = [int(i) for i in input().split(' ')]
    a = [int(i) for i in input().split(' ')]

    d_max = max(a)
    d_min = min(a)

    if k % 2 == 1:
        print(' '.join([str(d_max - c) for c in a]))
    else:
        print(' '.join([str(c - d_min) for c in a]))

    t -= 1
