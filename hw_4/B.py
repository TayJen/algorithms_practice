t = int(input())


def who_wins(s: str) -> None:
    binary_dict = {
        '0': 0, '1': 0
    }

    for digit in s:
        binary_dict[digit] += 1

    min_count_pairs = min(binary_dict['0'], binary_dict['1'])

    if min_count_pairs % 2 == 0:
        print('NET')
    else:
        print('DA')


while t:
    s = input()
    who_wins(s)
    t -= 1
