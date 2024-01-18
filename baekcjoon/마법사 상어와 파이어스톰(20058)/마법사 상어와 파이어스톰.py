import sys, collections
input = sys.stdin.readline


def rotate(l):
    new_board = [[0] * n for _ in range(n)]
    grid_size = 2 ** l
    empty = []
    for x in range(0, n, grid_size):
        for y in range(0, n, grid_size):
            for i in range(grid_size):
                for j in range(grid_size):
                    ice = board[x + j][y + i]
                    new_board[x + i][y + grid_size - j - 1] = ice
                    if ice == 0:
                        empty.append([x+i, y+grid_size-j-1])
    return new_board, empty


def melt():
    ice_cnt = [[1] + [2] * (n - 2) + [1] for _ in range(n)]

    for y in range(n):
        ice_cnt[0][y] -= 1
        ice_cnt[n-1][y] -= 1

    for x, y in empty_area:
        for dx, dy in move:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                ice_cnt[nx][ny] -= 1

    for i in range(n):
        for j in range(n):
            if temp_board[i][j] and ice_cnt[i][j] < 1:
                temp_board[i][j] -= 1

    return temp_board


def ice_count():
    visited = [[False] * n for _ in range(n)]
    max_cnt = 0
    total_ice = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] and not visited[i][j]:
                cnt = 1
                q = collections.deque([[i, j]])
                visited[i][j] = True
                sum_ice = board[i][j]
                while q:
                    x, y = q.popleft()
                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny]:
                            q.append([nx, ny])
                            visited[nx][ny] = True
                            sum_ice += board[nx][ny]
                            cnt += 1

                max_cnt = max(max_cnt, cnt)
                total_ice += sum_ice
    print(total_ice)
    print(max_cnt)


N, Q = map(int, input().split())
n = 2 ** N
board = [list(map(int, input().split())) for _ in range(n)]
L = list(map(int, input().split()))
move = ((1, 0), (0, 1), (-1, 0), (0, -1))
for level in L:
    temp_board, empty_area = rotate(level)
    board = melt()

ice_count()
