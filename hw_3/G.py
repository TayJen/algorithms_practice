import sys


stack = []

n = int(input())
raw_input = sys.stdin.readlines()
for operation in raw_input:
    if operation[0] == '1':
        stack.append(operation.split(' ')[1])
    else:
        print(stack.pop())


