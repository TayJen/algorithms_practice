import sys

def extended_gcd(a: int, b: int) -> None:
    if b == 0:
        gcd = a
        x = 1
        y = 0
    else:
        gcd, y, x = extended_gcd(b, a % b)
        y = y - (a // b) * x

    return gcd, x, y 


m = int(input())
while m:
    a, b = map(int, sys.stdin.readline().split(' '))
    _, x, y = extended_gcd(a, b)
    print(x, y)
    m -= 1
