t = int(input())

def lowest_cells_change(n: int, m: int, grid):
    count_cells = 0

    for i in range(m - 1):
        if grid[n-1][i] != 'R':
            count_cells += 1

    for i in range(n - 1):
        if grid[i][m-1] != 'D':
            count_cells += 1

    return count_cells


while t:
    n, m = [int(i) for i in input().split(' ')]

    grid = [list(input()) for _ in range(n)]
    print(lowest_cells_change(n, m, grid))

    t -= 1