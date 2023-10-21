def minDistance(word1: str, word2: str) -> int:
    dp = [[None] * (len(word1) + 1) for _ in range(len(word2) + 1)]

    for i in range(len(word1) + 1):
        dp[len(word2)][i] = len(word1) - i

    for i in range(len(word2) + 1):
        dp[i][len(word1)] = len(word2) - i

    for i in range(len(word2) - 1, -1, -1):
        for j in range(len(word1) - 1, -1, -1):
            if word2[i] == word1[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

    # for i in range(len(dp)):
    #     for j in range(len(dp[i])):
    #         print(dp[i][j], end=' ')
    #     print()

    return dp[0][0]

if __name__ == "__main__":
    a = input()
    b = input()

    print(minDistance(a, b))