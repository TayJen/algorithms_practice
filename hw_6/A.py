def find_floor(n, x):
    if n < 3:
        return 1
    else:
        return (n - 3) // x + 2


t = int(input())
while t:
    n, x = [int(i) for i in input().split()]
    print(find_floor(n, x))
    t -= 1
