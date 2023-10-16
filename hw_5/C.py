class Node:
    def __init__(self, val: int):
        self.val = val
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None
        self.height: int = 1


class AVL:
    def __init__(self):
        self.root = None

    def find(self, val: int) -> Node:
        curr = self.root
        while curr:
            if curr.val == val:
                return curr
            elif curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def find_prev_val(self, val: int) -> int:
        curr = self.root
        prev_val = None
        while curr:
            if curr.val < val:
                prev_val = curr.val
                curr = curr.right
            else:
                curr = curr.left
        return prev_val

    def find_next_val(self, val: int) -> int:
        curr = self.root
        next_val = None
        while curr:
            if curr.val > val:
                next_val = curr.val
                curr = curr.left
            else:
                curr = curr.right
        return next_val

    def insert(self, val: int) -> None:
        # If node is already in the tree, then do nothing
        if self.find(val):
            return

        # If its the first inserted node then its root
        if self.root is None:
            self.root = Node(val)
            return

        val_node = Node(val)
        curr = self.root

        # Find place where to insert
        while curr:
            if val < curr.val and curr.left is not None:
                curr = curr.left
            elif val > curr.val and curr.right is not None:
                curr = curr.right

            elif val < curr.val and curr.left is None:
                curr.left = val_node
                val_node.parent = curr
                break
            elif val > curr.val and curr.right is None:
                curr.right = val_node
                val_node.parent = curr
                break


    def remove(self, val: int) -> None:
        # If val_node doesn't exists, then we do nothing
        val_node = self.find(val)
        if val_node is None:
            return



        if val_node.left is None:
            # If current node has no parent (its root)
            if val_node.parent is None and self.root == val_node:
                self.root = val_node.right

            # If current node is to the left of the parent
            elif val_node.parent.left == val_node:
                val_node.parent.left = val_node.right

            # If current node is to the right of the parent
            elif val_node.parent.right == val_node:
                val_node.parent.right = val_node.right

            # Remember parent to the node inserted instead of the deleted one
            if val_node.right is not None:
                val_node.right.parent = val_node.parent

            del val_node
        else:
            # Find predecessor (with one left kid or with no kids)
            curr = val_node.left
            while curr.right:
                curr = curr.right

            # Swap predecessor val and deleting node val
            val_node.val, curr.val = curr.val, val_node.val

            # Predecessor is removed, parent for the predecessor parent is remembered
            if curr.parent is not None:
                if curr.parent == val_node:
                    curr.parent.left = curr.left
                else:
                    curr.parent.right = curr.left
            if curr.left is not None:
                curr.left.parent = curr.parent

            del curr

    def left_rotate(self, val_node: Node) -> None:


    def rebalance(self):
        pass

    def print_tree(self, curr, indent, last):
        if curr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(curr.val)
            self.print_tree(curr.left, indent, False)
            self.print_tree(curr.right, indent, True)



tree = AVL()

import sys

# for oper in sys.stdin.readlines():

while True:
    oper = input()


    command, value = oper.split(' ')
    value = int(value)

    if command == "insert":
        tree.insert(value)
    elif command == "delete":
        tree.remove(value)
    elif command == "exists":
        answer = tree.find(value)
        if answer is not None:
            print('true')
        else:
            print('false')
    elif command == 'prev':
        answer = tree.find_prev_val(value)
        if answer is not None:
            print(answer)
        else:
            print('none')
    elif command == 'next':
        answer = tree.find_next_val(value)
        if answer is not None:
            print(answer)
        else:
            print('none')

    tree.print_tree(tree.root, "", True)
