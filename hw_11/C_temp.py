import sys


s = input() + "$"
n = len(s)


p = sorted(range(len(s)), key=lambda i: s[i:])

c = [0] * n
for i in range(n):
    c[p[i]] = i

l = [0] * n
k = 0
for i in range(n):
    x = c[i]        # позиция в суффиксном массиве
    if not x:
        continue
    if k > 0:
        k -= 1
    while s[p[x-1] + k] == s[p[x] + k]:
        k += 1
    l[x-1] = k

m = int(input())
while m:
    a, b = map(int, sys.stdin.readline().split(' '))
    if a == b:
        print(n - a - 1)
    else:
        pos_a = min(c[a], c[b])
        pos_b = max(c[a], c[b])
        print(min(l[pos_a: pos_b]))

    m -= 1
