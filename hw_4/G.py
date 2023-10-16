n = int(input())
heap = [int(i) for i in input().split(' ')]

for i in range(1, n+1):
    if 2*i+1 <= n and heap[2*i] < heap[i-1] or 2*i <= n and heap[2*i-1] < heap[i-1]:
        print('NO')
        break
else:
    print('YES')