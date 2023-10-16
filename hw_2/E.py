N, k = [int(i) for i in input().split(' ')]
shoes = [int(i) for i in input().split(' ')]


shoes.sort()
repaired_shoes = 0
for shoe_time in shoes:
    N -= shoe_time

    if N >= 0:
        repaired_shoes += 1

    if N <= 0:
        break

print(repaired_shoes)