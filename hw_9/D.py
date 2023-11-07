n, S = [int(i) for i in input().split(' ')]
# so that the numeration is from 1 instead of zero, first item, second and etc.
weight = [0] + [int(i) for i in input().split(' ')]
cost = [0] + [int(i) for i in input().split(' ')]

# d[i, j] - is the maximum price from first i items with weight j
# so basically j is less then S, and with any amount of items
# we can always add up to 0 weight.
dp = []
for _ in range(n+1):
    dp.append([0] * (S+1))

# for restoring the answer
d_taken = []
for _ in range(n+1):
    d_taken.append([False] * (S+1))

for i in range(1, n+1):
    for j in range(1, S+1):
        if j - weight[i] >= 0 and dp[i-1][j-weight[i]] + cost[i] >= dp[i-1][j]:
            dp[i][j] = dp[i-1][j-weight[i]] + cost[i]
            d_taken[i][j] = True
        else:
            dp[i][j] = dp[i-1][j]

# for i in range(n+1):
#     for j in range(S+1):
#         print(dp[i][j], end=' ')
#     print()

# for i in range(n+1):
#     for j in range(S+1):
#         print(d_taken[i][j], end=' ')
#     print()

# Restore answer
j_max = 0
for j in range(1, S+1):
    if dp[n][j] > dp[-1][j_max]:
        j_max = j

ans = ""
count = 0
i = n
while j_max or i:
    if d_taken[i][j_max] is True:
        ans = str(i) + " " + ans
        j_max -= weight[i]
        count += 1
    i -= 1
print(count)
print(ans.strip())
