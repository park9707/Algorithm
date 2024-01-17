import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
fireball_cnt = [[0] * N for _ in range(N)]
stack = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append([m, s, d])
    stack.append([r-1, c-1])
move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(K):
    temp = set()
    next_board = [[[] for _ in range(N)] for _ in range(N)]
    for r, c in stack:
        for i in range(len(board[r][c])):
            m, s, d = board[r][c][i]
            nr, nc = (r + move[d][0] * s) % N, (c + move[d][1] * s) % N
            temp.add((nr, nc))
            next_board[nr][nc].append([m, s, d])

    board = next_board
    stack = []
    for x, y in temp:
        n = len(board[x][y])
        if n > 1:
            temp_board = []
            direction = 0
            d = board[x][y][0][2] % 2
            sum_m = board[x][y][0][0]
            sum_s = board[x][y][0][1]
            for i in range(1, n):
                if board[x][y][i][2] % 2 != d and direction == 0:
                    direction = 1
                sum_m += board[x][y][i][0]
                sum_s += board[x][y][i][1]
            if sum_m // 5 == 0:
                continue
            board[x][y] = [[sum_m // 5, sum_s // n, j] for j in range(direction, 8, 2)]
        stack.append([x, y])

ans = 0

for i, j in stack:
    for k in range(len(board[i][j])):
        ans += board[i][j][k][0]

print(ans)