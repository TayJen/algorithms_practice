N, k = [int(i) for i in input().split(' ')]
coins = [int(i) for i in input().split(' ')] + [0]

# First value is the coins summa, second is the path
coins_max = [(0, [1])] * (N + k - 1)

for i in range(k, N + k - 1):
    max_idx = None
    for j in range(i-k, i):
        if max_idx is None or coins_max[j][0] > coins_max[max_idx][0]:
            max_idx = j

    coins_max[i] = (coins_max[max_idx][0] + coins[i - k], coins_max[max_idx][1] + [i - k + 2])


print(coins_max[-1][0])
print(len(coins_max[-1][1]) - 1)
print(' '.join(map(str, coins_max[-1][1])))
