import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
board = []
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
board = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    if board[i][0] == -1:
        clean = [i, i+1]
        break


def clean_up():
    up_move = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    x, y = clean[0], 0
    pre = 0
    for dx, dy in up_move:
        while True:
            x += dx
            y += dy
            if x == -1 or x == clean[1] or y == -1 or y == c:
                break
            board[x][y], pre = pre, board[x][y]
        x -= dx
        y -= dy


def clean_down():
    down_move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y = clean[1], 0
    pre = 0
    for dx, dy in down_move:
        while True:
            x += dx
            y += dy
            if x == clean[0] or x == r or y == -1 or y == c:
                break
            board[x][y], pre = pre, board[x][y]
        x -= dx
        y -= dy


for _ in range(t):
    tmp_board = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                cnt = 0
                n = board[i][j] // 5
                for dx, dy in move:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < r and 0 <= ny < c:
                        if nx not in clean or ny != 0:
                            tmp_board[nx][ny] += n
                            cnt += 1
                board[i][j] -= (n * cnt)

    for i in range(r):
        for j in range(c):
            board[i][j] += tmp_board[i][j]

    clean_up()
    clean_down()

    board[clean[0]][0] = board[clean[1]][0] = -1

print(sum([dust[i] for dust in board for i in range(c)]) + 2)
