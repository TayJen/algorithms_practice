import sys


s1 = input() + "$"
s2 = len(s)

# У строки abbaab столько же суффиксов сколько и ее длина:

#      0,     1,    2,   3,  4, 5
# abbaab, bbaab, baab, aab, ab, b - все суффиксы

# a b b a a b
# 0 1 2 3 4 5

# получаем суффиксный массив, отсортированный в порядке лексикографического возрастания
# (aab, ab, abbaab, b, baab, bbaab)
# 3, 4, 0, 5, 2, 1 - с какого символа начинается суффикс
p = [t[1] for t in sorted((s[i:], i) for i in range(len(s)))]
# print(p)

# исходные позиции суффиксов, по тому с какой позиции начинается суффикс
# получаем его положение в суффиксном отсортированном массиве
c = [0] * n
for i in range(n):
    c[p[i]] = i
# print(c)

# между двумя соседними суффиксами в суффиксном массиве находим
# максимальную длину префикса
l = [0] * n
k = 0
for i in range(n):
    x = c[i]    # позиция в суффиксном массиве
    if not x:
        continue
    if k > 0:
        k -= 1
    while s[p[x-1] + k] == s[p[x] + k]:
        k += 1
    l[x-1] = k
# print(l)

m = int(input())
while m:
    a, b = map(int, sys.stdin.readline().split(' '))
    pos_1 = min(c[a], c[b])
    pos_2 = max(c[a], c[b])
    print(min(l[pos_1: pos_2]))

    m -= 1
