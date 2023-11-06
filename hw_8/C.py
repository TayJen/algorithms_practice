n = int(input())
s1 = [int(i) for i in input().split(' ')]
m = int(input())
s2 = [int(i) for i in input().split(' ')]

dp = []

for _ in range(n + 1):
    dp.append([0] * (m + 1))

# Find maximum
for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])

# Restore answer
answer = ""
i, j = n, m
while True:
    if i == 0 or j == 0:
        break
    if s1[i-1] == s2[j-1]:
        answer = str(s1[i-1]) + ' ' + answer
        i -= 1
        j -= 1
    elif dp[i-1][j] == dp[i][j]:
        i -= 1
    else:
        j -= 1

print(answer.strip())
