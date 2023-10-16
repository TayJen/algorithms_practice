import sys

class Queue():
    def __init__(self):
        self.M = 100000
        self.queue = [0] * self.M
        self.head = self.tail = 0

    def enqueue(self, val: int):
        self.queue[self.tail % self.M] = val
        self.tail += 1

    def dequeue(self):
        val = self.queue[self.head % self.M]
        self.head += 1
        return val


n = int(input())
q = Queue()

raw_input = sys.stdin.readlines()

for oper in raw_input:
    if oper[0] == '+':
        q.enqueue(int(oper.split(' ')[1]))
    else:
        print(q.dequeue())