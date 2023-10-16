def find_is_good(tiles, m):
    if m % 2 == 1:
        print('NO')
    else:
        flag_main = False
        for tile in tiles:
            if tile[0][1] == tile[1][0]:
                flag_main = True
        if flag_main:
            print('YES')
        else:
            print('NO')

t = int(input())
while t:
    n, m = [int(i) for i in input().split()]
    tiles = []
    for _ in range(n):
        tile = []
        tile.append([int(i) for i in input().split()])
        tile.append([int(i) for i in input().split()])
        tiles.append(tile)
    find_is_good(tiles, m)
    t -= 1
