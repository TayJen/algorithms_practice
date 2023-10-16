n = int(input())
heights = [int(i) for i in input().split(' ')]
looking_ways = input()

answer_visible = [0] * len(heights)

class OnlyDecreasingStack():
    def __init__(self):
        self.stack = []

    def len_stack(self):
        return len(self.stack)

    def add_stack(self, val: int):
        # print('Start', self.stack)
        if not self.stack:
            # print('Am I Right')
            self.stack.append(val)
        else:
            for _ in range(-1, -(len(self.stack)+1), -1):
                last_val = self.stack.pop()
                # print(last_val)
                if last_val >= val:
                    # print('Really nigga')
                    self.stack.append(last_val)
                    self.stack.append(val)
                    break
            else:
                # print('Here')
                self.stack.append(val)
        # print('Finish', self.stack)

    def clear(self):
        self.stack = []

main = OnlyDecreasingStack()

for i in range(n):
    look_way = looking_ways[i]
    curr_soldier_height = heights[i]

    if look_way == 'L':
        answer_visible[i] = main.len_stack()
        main.add_stack(curr_soldier_height)
    else:
        main.add_stack(curr_soldier_height)


main.clear()

for i in range(n-1, -1, -1):
    look_way = looking_ways[i]
    curr_soldier_height = heights[i]

    if look_way == 'R':
        answer_visible[i] = main.len_stack()
        main.add_stack(curr_soldier_height)
    else:
        main.add_stack(curr_soldier_height)

print(' '.join([str(i) for i in answer_visible]))