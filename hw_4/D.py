import sys

class Deque():
    def __init__(self):
        self.M = 2
        self.deque = [None] * self.M
        self.head = self.tail = 0

    def pop_front(self):
        self.head += 1
        val = self.deque[self.head % self.M]
        self.deque[self.head % self.M] = None
        return val

    def pop_back(self):
        self.tail -= 1
        val = self.deque[self.tail % self.M]
        self.deque[self.tail % self.M] = None
        return val

    def push_front(self, val: int):
        if self.deque[self.head % self.M] is not None:
            self.more_space()

        self.deque[self.head % self.M] = val
        if self.head == self.tail:
            self.tail += 1
        self.head -= 1

    def push_back(self, val: int):
        if self.deque[self.tail % self.M] is not None:
            self.more_space()

        self.deque[self.tail % self.M] = val
        if self.head == self.tail:
            self.head -= 1

        self.tail += 1

    def more_space(self):
        self.deque = [self.pop_front() for _ in range(self.M)] + [None] * self.M
        self.head = -1
        self.tail = self.M
        self.M *= 2


n = int(input())
dict_deqs = {}


for oper in sys.stdin.readlines():
    oper_lst = oper.split(' ')
    command = oper_lst[0]
    deque_num = int(oper_lst[1])

    if "push" == command[:4] and deque_num not in dict_deqs:
        dict_deqs[deque_num] = Deque()

    if command == "pushfront":
        dict_deqs[deque_num].push_front(int(oper_lst[2]))

    elif command == "pushback":
        dict_deqs[deque_num].push_back(int(oper_lst[2]))

    elif command == "popfront":
        print(dict_deqs[deque_num].pop_front())

    elif command == "popback":
        print(dict_deqs[deque_num].pop_back())

    # print(dict_deqs[1].deque, dict_deqs[1].head, dict_deqs[1].tail)
