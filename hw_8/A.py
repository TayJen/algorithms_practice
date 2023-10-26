from typing import List


def can_be_rotated(a_list: List[int], b_list: List[int], x: int) -> bool:
    a_sorted = sorted(a_list, reverse=False)
    b_sorted = sorted(b_list, reverse=True)

    for a_val, b_val in zip(a_sorted, b_sorted):
        if a_val + b_val > x:
            return False

    return True


def main():
    t = int(input())
    while t:
        n, x = [int(i) for i in input().split()]
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        if t > 1:
            input()

        if can_be_rotated(a, b, x):
            print('Yes')
        else:
            print('No')

        t -= 1

if __name__ == "__main__":
    main()
