n, m = [int(i) for i in input().split(' ')]
fines = []
visited = []

for _ in range(n):
    fines.append([int(i) for i in input().split(' ')])
    visited.append([0] * m)


def change_value(row: int, col: int):
    visited[row][col] = 1
    if row == 0 and col == 0:
        pass

    elif row > 0 and col == 0:
        fines[row][col] = find_min_curr(row-1, col) + fines[row][col]

    elif row == 0 and col > 0:
        fines[row][col] = find_min_curr(row, col-1) + fines[row][col]

    else:
        fines[row][col] = min(find_min_curr(row-1, col), find_min_curr(row, col-1)) + fines[row][col]


def find_min_curr(row: int, col: int) -> int:
    if visited[row][col]:
        return fines[row][col]
    else:
        change_value(row, col)
        return fines[row][col]

print(find_min_curr(n-1, m-1))
