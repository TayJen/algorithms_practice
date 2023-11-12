from typing import Tuple, List
from random import randint
import sys


class ImplicitTreap:
    def __init__(self, x: int, left_treap=None, right_treap=None):
        self.x: int = x
        self.y: int = randint(1, 150000)
        self.left: ImplicitTreap = left_treap
        self.right: ImplicitTreap = right_treap

        self.size: int = 1
        self.reversed = False


def merge(L: ImplicitTreap, R: ImplicitTreap) -> ImplicitTreap:
    push(L)
    push(R)
    if L is None:
        return R
    if R is None:
        return L

    if L.y > R.y:
        L.right = merge(L.right, R)
        recalc(L)
        return L
    else:
        R.left = merge(L, R.left)
        recalc(R)
        return R


def split(T: ImplicitTreap, x0: int) -> Tuple[ImplicitTreap, ImplicitTreap]:
    push(T)
    if T is None:
        return (None, None)

    if get_size(T.left) < x0:
        L, R = split(T.right, x0 - get_size(T.left) - 1)
        T.right = L
        recalc(T)
        return (T, R)
    else:
        L, R = split(T.left, x0)
        T.left = R
        recalc(T)
        return (L, T)


def get_size(T: ImplicitTreap):
    if T is None:
        return 0
    else:
        return T.size


def recalc(T: ImplicitTreap):
    if T is not None:
        T.size = get_size(T.left) + get_size(T.right) + 1


def push(T: ImplicitTreap):
    if T is None:
        return
    if T.reversed is False:
        return

    T.reversed = False
    T.left, T.right = T.right, T.left
    if T.left is not None:
        T.left.reversed ^= True
    if T.right is not None:
        T.right.reversed ^= True


def reverse(T: ImplicitTreap, A: int, B: int) -> ImplicitTreap:
    # Split by left if A = 3, B = 7 <=> [1, 2, 3, 4, 5, 6, 7, 8] -> [1, 2, 3] & [4, 5, 6, 7, 8]
    L, R = split(T, A - 1)

    # Split by right [4, 5, 6, 7, 8, 9] -> [4, 5, 6, 7] & [8]
    M, R = split(R, B - A + 1)
    M.reversed ^= True

    return merge(merge(L, M), R)


def print_tree(T: ImplicitTreap):
    if T is None:
        return
    push(T)
    print_tree(T.left)
    print(T.x, end=' ')
    print_tree(T.right)


def from_list(arr: List[int]) -> ImplicitTreap:
    result = None
    for val in arr:
        result = merge(result, ImplicitTreap(val))
    return result


if __name__ == "__main__":
    n, m = [int(i) for i in input().split(' ')]
    arr = [i for i in range(1, n+1)]

    main_T = from_list(arr)
    # print_tree(main_T)
    # print()

    while m:
        a, b = map(int, sys.stdin.readline().split(' '))
        reverse(main_T, a, b)
        # print_tree(main_T)
        # print()
        m -= 1

    print_tree(main_T)
