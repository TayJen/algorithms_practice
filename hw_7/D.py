N, k = [int(i) for i in input().split(' ')]

a = [1] * (k) + [0] * (N - k - 1)
# print(a)

for i in range(N - 1):
    for j in range(i-1, max(i-k-1, -1), -1):
        a[i] += a[j]

# print(a)
print(a[N - 2])
