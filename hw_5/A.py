t = int(input())

def find_indices(n, perm):
    for j in range(1, n-1):
        if perm[j-1] < perm[j] and perm[j+1] < perm[j]:
            print("YES")
            print(f"{j} {j+1} {j+2}")
            break
    else:
        print("NO")

while t:
    n = int(input())
    perm = [int(i) for i in input().split(' ')]
    find_indices(n, perm)

    t -= 1