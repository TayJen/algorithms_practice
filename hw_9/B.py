def find_coloring(T, a):
    lst = []
    c = {}
    d = {}

    for val in a:
        if (T - val) not in c:
            c[val] = 1
            lst.append(0)
        elif (T - val) in c and (T - val) not in d:
            d[val] = 1
            lst.append(1)
        elif (T - val) in c and (T - val) in d:
            if c[T - val] < d[T - val]:
                c[val] += 1
                lst.append(0)
            else:
                d[val] += 1
                lst.append(1)

    return lst


t = int(input())
while t:
    n, T = [int(i) for i in input().split(' ')]
    a = [int(i) for i in input().split(' ')]
    ans = find_coloring(T, a)
    print(' '.join(map(str, ans)))

    t -= 1
