import sys


class MinStack():
    def __init__(self):
        self.stack = []

    def add_element(self, val: int):
        # if stack is empty then the minimum is the first element
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.get_minimum())))

    def get_minimum(self):
        return self.stack[-1][1]    # last element, second value is the minimum

    def pop(self):
        return self.stack.pop()[0]  # last element, first value is the element


n = int(input())
min_stack = MinStack()

raw_input = sys.stdin.readlines()
for operation in raw_input:
    if operation[0] == '1':
        min_stack.add_element(int(operation.split(' ')[1]))
    elif operation[0] == '2':
        min_stack.pop()
    else:
        print(min_stack.get_minimum())

