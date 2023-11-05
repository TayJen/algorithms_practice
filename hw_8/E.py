def find_max(i, j):
    if i >= j:
        return 0
    if (s[i] + s[j]) in ("()", "[]", "{}"):
        return 2 + find_max(i + 1, j - 1)
    if s[i] != s[j]:
        return max(find_max(i+1, j), find_max(i, j-1))


s = input()
start, end = 0, len(s) - 1
print(find_max(start, end))
