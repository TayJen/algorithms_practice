t = int(input())

def find_similar_string(n: int, s: str):
    init_s = list(s[:n])
    for i in range(1, len(s)-n+1):
        new_s = s[i:i+n]
        for j in range(n):
            if new_s[j] == '1':
                init_s[j] = '1'

    return ''.join(init_s)


while t:
    n = int(input())
    s = input()

    print(find_similar_string(n, s))

    t -= 1