import sys
import random

def gcd(a: int, b: int) -> int:
    a0 = max(a, b)
    b0 = min(a, b)
    return a0 if b0 == 0 else gcd(a0 % b0, b0)

def log_pow(x, e, n):
    if e == 1:
        return x % n
    elif e % 2 == 1:
        return x * log_pow(x * x, (e - 1) // 2, n) % n
    else:
        return log_pow(x * x, e // 2, n) % n

def check_prime_approx(n: int) -> bool:
    a = random.randint(1, n-1)
    print(a)
    if gcd(a, n) != 1 or n % 2 == 0:
        # print("Thats why #1")
        return False

    n_1 = n - 1
    if log_pow(a, n_1, n) != 1:
        # print("Thats why #2")
        return False

    # num_2s = 0
    # y = n_1
    # while y % 2 == 0:
    #     num_2s += 1
    #     y = y // 2

    # a_y = log_pow(a, y, n)
    # double_a = 1

    # while num_2s:
    #     new_a = (a_y * log_pow(a, double_a, n)) % n
    #     double_a *= 2
    #     num_2s -= 1

    #     if abs(new_a) != 1:
    #         print(new_a, double_a)
    #         print("Thats why #3")
    #         return False

    return True



m = int(input())

while m:
    n = int(sys.stdin.readline())

    for i in range(7):
        if not check_prime_approx(n):
            print('NO')
            break
    else:
        print('YES')

    m -= 1
