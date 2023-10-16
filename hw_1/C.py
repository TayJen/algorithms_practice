t = int(input())

def are_strings_similar(strings):
    dc_all_chars = {}

    for s in strings:
        for c in s:
            dc_all_chars[c] = dc_all_chars.get(c, 0) + 1

    for c in dc_all_chars:
        if dc_all_chars[c] % len(strings) != 0:
            print('NO')
            return

    print('YES')
    return

while t:
    n = int(input())
    strings = []

    for _ in range(n):
        strings.append(input())

    are_strings_similar(strings)
    t -= 1
