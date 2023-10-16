import sys

class Node():
    def __init__(self, val: int):
        self.next_node = None
        self.previous_node = None
        self.val = val


class MiddleQueue():
    def __init__(self):
        self.head = self.middle = self.tail = None
        self.overall_length = 0

    def push(self, val: int) -> None:
        self.overall_length += 1

        if self.overall_length == 1:
            self.first_push(val)
        else:
            new_node = Node(val)
            new_node.next_node = self.tail
            self.tail.previous_node = new_node
            self.tail = new_node

        if self.overall_length % 2 == 1 and self.middle.previous_node is not None:
            self.middle = self.middle.previous_node

    def pull(self) -> int:
        self.overall_length -= 1

        val = self.head.val

        if self.overall_length:
            self.head = self.head.previous_node
            self.head.next_node = None

            if self.overall_length % 2 == 1 and self.middle.previous_node is not None:
                self.middle = self.middle.previous_node
        else:
            self.head = self.middle = self.tail = None

        return val

    def first_push(self, val: int) -> None:
        self.tail = self.middle = self.head = Node(val)

    def push_middle(self, val: int) -> None:
        self.overall_length += 1

        if self.overall_length == 1:
            self.first_push(val)
        else:
            new_node = Node(val)
            new_node.next_node = self.middle
            new_node.previous_node = self.middle.previous_node

            if self.middle.previous_node is not None:
                self.middle.previous_node.next_node = new_node
            self.middle.previous_node = new_node

            if self.tail == self.middle:
                self.tail = new_node

            if self.overall_length % 2 == 1:
                self.middle = new_node

# def vis_all_queue():
#     node = q.head
#     print(q.head.val, q.middle.val, q.tail.val)

#     while node is not None:
#         print(node.val, end=' ')
#         node = node.previous_node
#     print()

n = int(input())
q = MiddleQueue()

for oper in sys.stdin.readlines():
    if oper[0] == '+':
        q.push(int(oper.split(' ')[1]))
    elif oper[0] == '*':
        q.push_middle(int(oper.split(' ')[1]))
    elif oper[0] == '-':
        print(q.pull())

    # print(oper[:-1])
    # vis_all_queue()
    # print()