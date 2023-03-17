from collections import deque


def solution(board):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n = len(board[0])
    m = len(board)
    visited = [[-1] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'R':
                visited[i][j] = 0
                q = deque([(j, i)])
            if board[i][j] == 'G':
                gx = j
                gy = i

    while q:
        x, y = q.popleft()
        temp_x, temp_y = x, y

        for i in range(4):
            move = 0
            nx = x + dx[i]
            ny = y + dy[i]

            while 0 <= nx < n and 0 <= ny < m and board[ny][nx] != 'D':
                move = 1
                nx += dx[i]
                ny += dy[i]

            if move == 1:
                nx -= dx[i]
                ny -= dy[i]

                if visited[ny][nx] == -1:
                    visited[ny][nx] = visited[temp_y][temp_x] + 1
                    q.append((nx, ny))

    return visited[gy][gx]
