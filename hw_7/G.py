k, n = [int(i) for i in input().split(' ')]
f = [int(i) for i in input().split(' ')]
a = [int(i) for i in input().split(' ')]

ost = 1000000000 + 7


def dot(x, y):
    res = []
    for i in range(len(x)):
        res.append(
            [
                sum(x[i][j] * y[j][k] for j in range(len(x[i]))) % ost 
                for k in range(len(y[0]))
            ]
        )
    return res


def power(x, e):
    ans = [
        [int(i == j) for i in range(len(x))]
        for j in range(len(x))
    ]
    while e > 0:
        if e % 2 == 1:
            ans = dot(ans, x)
        x = dot(x, x)
        e = e // 2

    return ans


if n < k:
    print(f[n] % ost, sum(f[:n + 1]) % ost)
else:
    fib_x = [[0 for _ in range(k + 1)] for _ in range(k + 1)]
    fib_x[0][0] = fib_x[0][1] = 1

    for i in range(len(a)):
        fib_x[1][i + 1] = a[i]

    for i in range(2, k + 1):
        fib_x[i][i - 1] = 1

    fib_x = power(fib_x, n - k + 2)
    f_val = [[sum(f[:-1])]] + [[val] for val in f[::-1]]
    res = dot(fib_x, f_val)

    print(res[2][0], res[0][0])
