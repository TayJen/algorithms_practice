n = int(input())
paths, dp, prev = [], [], []
for _ in range(n):
    paths.append([int(i) for i in input().split(' ')])
    dp.append([float('inf')] * (1 << n))
    prev.append([-1] * (1 << n))

dp[0][1] = 0

for mask in range(1, (1 << n)):
    for u in range(n):
        if mask & (1 << u) == 0:
            continue
        for v in range(n):
            if u != v and mask & (1 << v) != 0:
                if dp[v][mask ^ (1 << u)] + paths[v][u] < dp[u][mask]:
                    dp[u][mask] = dp[v][mask ^ (1 << u)] + paths[v][u]
                    prev[u][mask] = v

# Shortest path length
min_path = min(dp[u][(1 << n) - 1] for u in range(n))
print(min_path)

# Restoring the path
path = []
mask = (1 << n) - 1
u = min(range(n), key=lambda x: dp[x][(1 << n) - 1])
while mask > 0:
    path.append(u)
    v = prev[u][mask]
    mask ^= (1 << u)
    u = v

# Shortest path
print(' '.join(map(lambda x: str(x + 1), path)))
