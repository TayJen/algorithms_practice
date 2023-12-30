import sys

N = 2 * 1000000
prime_set = [0, 0] + [1] * N

for i in range(2, N):
    if prime_set[i]:
        for j in range(i * i, N, i):
            prime_set[j] = 0


m = int(input())

while m:
    n = int(sys.stdin.readline())

    if prime_set[n]:
        print('YES')
    else:
        print('NO')

    m -= 1