def is_dividible_3_almost_prime(n: int):
    if n - 6 - 10 - 14 > 0 and n - 6 - 10 - 14 != 6 and n - 6 - 10 - 14 != 10 and n - 6 - 10 - 14 != 14:
        print("YES")
        print(f"6 10 14 {n - 6 - 10 - 14}")
        return True
    elif n - 6 - 10 - 14 > 0:
        print("YES")
        print(f"6 10 15 {n - 6 - 10 - 15}")
        return True
    else:
        print("NO")
        return False


t = int(input())

while t:
    is_dividible_3_almost_prime(int(input()))
    t -= 1
