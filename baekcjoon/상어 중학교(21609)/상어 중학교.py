import sys
input = sys.stdin.readline


def count_block():
    visited = [[0] * N for _ in range(N)]
    blocks = []
    coordinate = []
    coordinate_idx = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visited[i][j]:
                num = board[i][j]
                stack = [[i, j]]
                visited[i][j] = num
                temp_coordinate = []
                block_cnt = 1
                rainbow_block = 0
                while stack:
                    x, y = stack.pop()
                    temp_coordinate.append([x, y])
                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] != num:
                            if board[nx][ny] == 0:
                                rainbow_block += 1
                            elif board[nx][ny] != num:
                                continue
                            stack.append([nx, ny])
                            visited[nx][ny] = num
                            block_cnt += 1

                if block_cnt > 1:
                    blocks.append([i, j, block_cnt, rainbow_block, coordinate_idx])
                    coordinate_idx += 1
                    coordinate.append(temp_coordinate)

    if blocks:
        global score
        _, _, cnt, _, coordinate_idx = sorted(blocks, key=lambda a: [a[2], a[3], a[0], a[1]], reverse=True)[0]
        score += cnt ** 2
        return coordinate[coordinate_idx]
    else:
        return []


def erase_block(arr):
    for x, y in arr:
        board[x][y] = -2


def gravity():
    def find_empty(a):
        while a > 0:
            if board[a][y] == -2:
                break
            a -= 1
        return a

    for y in range(N):
        r = find_empty(N-1)
        x = r - 1
        while x >= 0 and r > 0:
            if board[x][y] == -1:
                r = find_empty(x - 1)
                x = r
            elif board[x][y] >= 0:
                board[r][y], board[x][y] = board[x][y], -2
                r -= 1
            x -= 1


def rotate(pre_board):
    new_board = []
    for y in range(N-1, -1, -1):
        temp = []
        for x in range(N):
            temp.append(pre_board[x][y])
        new_board.append(temp)
    return new_board


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move = ((1, 0), (0, 1), (-1, 0), (0, -1))
score = 0

while True:
    blocks = count_block()
    if not blocks:
        break
    erase_block(blocks)
    gravity()
    board = rotate(board)
    gravity()

print(score)