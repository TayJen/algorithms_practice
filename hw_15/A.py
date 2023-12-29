n = int(input())

i = 2
while i * i <= n:
    if n % i == 0:
        print(i, end=' ')
        n = n // i
    else:
        i += 1
else:
    if n > 1:
        print(n)
