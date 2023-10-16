n = int(input())

def find_k(a, b):
    if a != b:
        return abs(a - b) // 10 + int(bool(abs(a - b) % 10))
    else:
        return 0

while n:
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    print(find_k(a, b))
    n -= 1

# print(find_k(5, 5))
# print(find_k(13, 42))
# print(find_k(18, 4))
# print(find_k(1337, 420))
# print(find_k(123456789, 1000000000))
# print(find_k(100500, 9000))