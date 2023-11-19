t, r = map(int, input().split(' '))
s = input()

hash = ord(s[0]) % r
print(hash)
for i in range(1, len(s)):
    hash = (hash * t + ord(s[i])) % r
    print(hash)
