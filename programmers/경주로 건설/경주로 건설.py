from collections import deque

def solution(board):
    q = deque([[0, 0, 4, 0]])
    n = len(board)
    visited = [[float("inf")] * n for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited[0][0] = 0

    while q:
        x, y, d, c = q.popleft()
        if x == n-1 and y == n-1:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == 0:
                if i == d:
                    nc = c + 100
                else:
                    nc = c + 600

                if visited[ny][nx] >= nc:
                    visited[ny][nx] = nc
                    q.append([nx, ny, i, nc])
                elif visited[ny][nx] >= nc - 500:
                    nx += dx[i]
                    ny += dy[i]
                    if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == 0:
                        if visited[ny][nx] > nc+100:
                            visited[ny][nx] = nc
                            q.append([nx, ny, i, nc+100])

    return visited[n-1][n-1]-500
