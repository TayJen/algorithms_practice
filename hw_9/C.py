S, n = [int(i) for i in input().split(' ')]
gold = [0] + [int(i) for i in input().split(' ')]

# d[i, j] - can we add up first i items to the weight j somehow?
# so basically j is less then S, and with any amount of items
# we can always add up to 0 weight.
dp = []
for _ in range(n+1):
    dp.append([True] + [False] * (S))

for i in range(1, n+1):
    for j in range(1, S+1):
        if j - gold[i] >= 0:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-gold[i]]
        else:
            dp[i][j] = dp[i-1][j]

for j in range(S, -1, -1):
    if dp[-1][j] is True:
        print(j)
        break
