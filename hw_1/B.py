t = int(input())

def is_tryangle_bad(s_lengths: str):
    lengths = [int(i) for i in s_lengths.split(' ')]

    lowest_0_idx = lengths.index(min(lengths[0], lengths[1], lengths[2]))
    highest_idx = lengths.index(max(lengths[0], lengths[1], lengths[2]))

    lowest_1_idx = [i for i in range(0, 3) if i != lowest_0_idx and i != highest_idx][0]

    for i in range(3, len(lengths)):
        if lengths[i] > lengths[highest_idx]:
            highest_idx = i
        elif lengths[i] < lengths[lowest_0_idx]:
            lowest_1_idx = lowest_0_idx
            lowest_0_idx = i
        elif lengths[i] < lengths[lowest_1_idx]:
            lowest_1_idx = i

    if lengths[lowest_0_idx] + lengths[lowest_1_idx] <= lengths[highest_idx]:
        print(' '.join([str(i) for i in sorted([lowest_0_idx + 1, lowest_1_idx + 1, highest_idx + 1])]))
    else:
        print(-1)

    return True

# t = 1
while t:
    n = int(input())
    # del n

    s = input()
    is_tryangle_bad(s)

    t -= 1