N = int(input())
row_digits = [int(i) for i in input().split(' ')]

def max_number(row_digits):
    count_digits = [0] * 10
    ans = ""

    for digit in row_digits:
        count_digits[digit] += 1

    for i, count_digit in enumerate(count_digits):
        ans = count_digit * str(i) + ans

    return ans

print(max_number(row_digits))