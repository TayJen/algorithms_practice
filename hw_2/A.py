t = int(input())

def lowest_password_length(password):
    true_pass = set(password)
    if len(true_pass) > 1:
        return 1
    else:
        return len(password)


while t:
    n = int(input())
    password = [int(i) for i in input().split(' ')]
    print(lowest_password_length(password))

    t -= 1