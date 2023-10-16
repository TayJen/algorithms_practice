C = float(input())

def find_x(C):
    l, r = 0, C
    eps = 1e-6

    while abs(r - l) > eps:
        mid = (l + r) / 2

        if mid * mid + mid ** 0.5 < C:
            l = mid
        else:
            r = mid

    return mid

print(round(find_x(C), 5))