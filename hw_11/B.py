import sys

hash_table = {}
powers = [1]

def precalc(s: str, t: int, r: int):
    hash = ord(s[0])
    hash_table[-1] = 0
    hash_table[0] = hash % r
    for i in range(1, len(s)):
        hash = (hash * t + ord(s[i])) % r
        hash_table[i] = hash


# Precompute a table of powers of t.
def find_power(s: str, t: int, r: int):
    for _ in range(1, len(s)+1):
        powers.append(powers[-1] * t % r)


def get_hash(r: int, a: int, b: int) -> int:
    if (a, b) in hash_table:
        return hash_table[(a, b)]

    val = (hash_table[b] - hash_table[a-1] * powers[b - a + 1] % r)
    if val < 0:
        val += r
    hash_table[(a, b)] = val
    return val


def main():
    t, r = map(int, input().split(' '))
    s = input()
    m = int(input())
    precalc(s, t, r)
    find_power(s, t, r)

    while m:
        a, b = map(int, sys.stdin.readline().split(' '))
        print(get_hash(r, a, b))
        m -= 1


main()
