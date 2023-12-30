N = 500000
prime_set = [0, 0] + [1] * N
a, b = map(int, input().split(' '))

for i in range(2, b + 1):
    if prime_set[i]:
        if i >= a:
            print(i, end=' ')

        for j in range(i * i, b + 1, i):
            prime_set[j] = 0
