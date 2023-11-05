import sys

N, K = [int(i) for i in input().split()]
arr = [0] * (N + 1)


for oper in sys.stdin.readlines():
    command, a, b = oper.split(' ')
    if command == 'A':
        idx = int(a) - 1
        val = int(b)
        arr[idx] = val
    elif command == 'Q':
        l = int(a) - 1
        r = int(b)
        print(sum(arr[l:r]))
