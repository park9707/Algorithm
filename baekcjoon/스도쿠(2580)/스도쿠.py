import sys
input = sys.stdin.readline

board = [list(map(int, input().rstrip().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))
cnt = len(blank)


def check_partition(x, y, num):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if board[i][j] == num:
                return False
    return True


def check_row(x, num):
    for i in range(9):
        if board[x][i] == num:
            return False
    return True


def check_col(y, num):
    for i in range(9):
        if board[i][y] == num:
            return False
    return True


def dfs(n):
    if n == cnt:
        for i in range(9):
            print(*board[i])
        exit(0)

    x = blank[n][0]
    y = blank[n][1]

    for target in range(1, 10):
        if check_col(y, target) and check_row(x, target):
            if check_partition(x // 3 * 3 if x != 0 else 0, y // 3 * 3 if y != 0 else 0, target):
                board[x][y] = target
                dfs(n+1)
                board[x][y] = 0


dfs(0)
