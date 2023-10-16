t = int(input())


while t:
    n = int(input())
    visited = set()
    for elem in input().split(' '):
        if elem not in visited:
            print(elem, end=' ')
            visited.add(elem)

    t -= 1