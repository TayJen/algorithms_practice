dp = []
a = []
n = 0
length = 0

def total_path():
    global n, length, dp, a
    res = 0
    for i in range(n):
        for j in range(length):
            dp[i][j] = float("inf")
    dp[0][0] = 0
    res = calculate_path(0, length - 1)
    return res

def calculate_path(i, j):
    global dp, a
    if dp[i][j] != float("inf"):
        return dp[i][j]
    for e in range(n):
        bit = ((j & (1 << e)) != 0)
        if a[i][e] != 0 and bit:
            dp[i][j] = min(dp[i][j], (calculate_path(e, j - (1 << e)) + a[i][e]))
    return dp[i][j]

def restore_path():
    global n, length, dp, a
    way = []
    i = 0
    j = length - 1
    while j != 0:
        for e in range(n):
            bit = ((j & (1 << e)) != 0)
            if a[i][e] != 0 and bit and dp[i][j] == dp[e][j - (1 << e)] + a[i][e]:
                way.append(e)
                i = e
                j = j - (1 << e)
    return way

n = int(input()) + 1
a = []
length = 1 << n
dp = [[0] * length for _ in range(n)]

for i in range(n):
    if i == 0:
        a.append([0] + [-1] * (n - 1))
    else:
        a.append([-1] + list(map(int, input().split())))

res = total_path()
print(res + 2)
ans = restore_path()

for i in range(len(ans) - 2, -1, -1):
    print(ans[i], end=" ")
