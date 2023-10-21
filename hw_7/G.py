k, n = [int(i) for i in input().split(' ')]
f = [int(i) for i in input().split(' ')]
a = [int(i) for i in input().split(' ')]



def fib(n):
    # the difference is dtype=object, it will let python do the calculation
    matrix = np.matrix([[1, 1], [1, 0]], dtype=object) ** abs(n)
    if n % 2 == 0 and n < 0:
        return -matrix[0,1]
    return matrix[0, 1]

if k <= n:
    s = sum(f)
    f_n = f[-1]

    i = len(f)
    while i <= n:
        f_n = 

        i += 1
else:
    s = sum(f[:n])
    f_n = f[n]