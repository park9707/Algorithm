import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
rotate_x = [0, 0, 0, 0]
rotate_y = [0, 0, 0, 0]

maps = [list(map(int, input().split())) for _ in range(n)]
move = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
commands = list(map(int, input().split()))


def change_y():
    if maps[x][y] == 0:
        maps[x][y] = rotate_y[2]
    else:
        rotate_y[2] = maps[x][y]
        maps[x][y] = 0


def change_x():
    if maps[x][y] == 0:
        maps[x][y] = rotate_x[2]
    else:
        rotate_x[2] = maps[x][y]
        maps[x][y] = 0


for command in commands:
    dx, dy = move[command]
    if 0 <= x + dx < n and 0 <= y + dy < m:
        x += dx
        y += dy
        if command <= 2:
            if dy < 0:
                rotate_y = rotate_y[1:] + rotate_y[:1]
                change_y()
            else:
                rotate_y = rotate_y[3:] + rotate_y[:3]
                change_y()
            rotate_x[0], rotate_x[2] = rotate_y[0], rotate_y[2]
            print(rotate_y[0])
        else:
            if dx < 0:
                rotate_x = rotate_x[1:] + rotate_x[:1]
                change_x()
            else:
                rotate_x = rotate_x[3:] + rotate_x[:3]
                change_x()
            rotate_y[0], rotate_y[2] = rotate_x[0], rotate_x[2]
            print(rotate_x[0])
