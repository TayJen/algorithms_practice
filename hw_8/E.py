def longest_correct_bracket_subsequence(s: str):
    n = len(s)

    dp = []
    for i in range(n):
        dp.append([0] * n)

    for i in range(n-1):
        if (s[i] + s[i + 1]) in ("()", "[]", "{}"):
            dp[i][i + 1] = 2

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if (s[i] + s[j]) in ("()", "[]", "{}"):
                dp[i][j] = 2 + dp[i+1][j-1]
            for k in range(i, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j])

    return dp[0][n-1]


print(longest_correct_bracket_subsequence(input()))
