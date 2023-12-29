def gcd(a: int, b: int) -> int:
    a0 = max(a, b)
    b0 = min(a, b)
    return a0 if b0 == 0 else gcd(a0 % b0, b0)

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


a, b = map(int, input().split(' '))
print(gcd(a, b), lcm(a, b))
