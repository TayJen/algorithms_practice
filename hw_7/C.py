n = int(input())
ladder = [int(i) for i in input().split(' ')]
ladder_max = [0] * (n + 2)

for i in range(2, n + 2):
    ladder_max[i] = max(ladder_max[i - 2], ladder_max[i - 1]) + ladder[i - 2]

# print(ladder_max)
print(ladder_max[-1])
