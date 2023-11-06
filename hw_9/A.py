def find_4_wall(a, b, c):
    return max(a, b, c)


t = int(input())
while t:
    a, b, c = [int(i) for i in input().split(' ')]
    print(find_4_wall(a, b, c))
    t -= 1
