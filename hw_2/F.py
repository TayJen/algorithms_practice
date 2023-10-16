N = int(input())
commands_res = []

for command_num in range(1, N+1):
    commands_res.append([int(score) for score in input().split(' ')] + [command_num])

commands_res = sorted(commands_res, key = lambda x: (-x[0], x[1], x[2]))

for _, _, command_num in commands_res:
    print(command_num, end=' ')