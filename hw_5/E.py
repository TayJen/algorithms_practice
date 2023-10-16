import sys
from typing import Tuple


class Node():
    def __init__(self, val: int):
        self.val = val
        self.l: Node = None
        self.r: Node = None


class BalancedSearchTree():
    def __init__(self):
        self.head: Node = None

    def exists(self, x: int) -> bool:
        if self.head:
            curr_node = self.head
            while curr_node:
                if curr_node.val == x:
                    return True

                if curr_node.val < x:
                    curr_node = curr_node.r
                elif curr_node.val > x:
                    curr_node = curr_node.l

        return False

    def insert(self, x: int) -> None:
        if not self.exists(x):
            node_l, node_r = self.split(self.head, x)
            n_node = Node(x)
            self.head = self.merge(node_l, self.merge(n_node, node_r))

    def delete(self, x: int) -> None:
        if self.exists(x):
            node_l, node_r = self.split(self.head, x)
            node_l_no_x, _ = self.split(node_l, x-1)
            self.head = self.merge(node_l_no_x, node_r)

    def next(self, x: int) -> int:
        _, node_r = self.split(self.head, x)
        curr_node, next_x = node_r, None
        while curr_node:
            next_x = curr_node.val
            curr_node = curr_node.l
        return next_x

    def prev(self, x: int) -> int:
        node_l, _ = self.split(self.head, x)
        curr_node, prev_x = node_l, None
        while curr_node:
            prev_x = curr_node.val
            curr_node = curr_node.r
        return prev_x

    def merge(self, node_l: Node, node_r: Node) -> Node:
        if node_l is None:
            return node_r
        if node_r is None:
            return node_l

        if node_l.val < node_r.val:
            node_l.r = self.merge(node_l.r, node_r)
            return node_l
        else:
            node_r.l = self.merge(node_l, node_r.l)
            return node_r

    def split(self, n_node: Node, x: int) -> Tuple[Node, Node]:
        if n_node is None:
            return (None, None)
        if n_node.val <= x:
            node_l, node_r = self.split(n_node.r, x)
            n_node.r = node_l
            return (n_node, node_r)
        else:
            node_l, node_r = self.split(n_node.l, x)
            n_node.l = node_r
            return (node_l, n_node)

    def output(self, node: Node, length: int) -> None:
        if node is not None:
            self.output(node.r, length + 1)
            print('      ' * length + str(node.val))
            self.output(node.l, length + 1)


tree = BalancedSearchTree()
n = int(input())

while n:
# for oper in sys.stdin.readlines():
    oper = input()
    command, x = oper.split(' ')
    x = int(x)

    if command == "exists":
        if tree.exists(x):
            print('true')
        else:
            print('false')

    elif command == "insert":
        tree.insert(x)

    elif command == "delete":
        tree.delete(x)

    elif command == "next":
        val = tree.next(x)
        if val:
            print(val)
        else:
            print('none')

    elif command == "prev":
        val = tree.prev(x)
        if val:
            print(val)
        else:
            print('none')

    tree.output(tree.head, 0)
    n -= 1
