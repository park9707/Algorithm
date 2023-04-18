from collections import deque


def solution(maps):
    n = len(maps[0])
    m = len(maps)
    visited = [[-1] * n for _ in range(m)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs():
        q = deque()
        q.append([0, 0])
        visited[0][0] = 1

        while q:
            x, y = q.popleft()

            if x == n - 1 and y == m - 1:
                return

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and maps[ny][nx] == 1:
                    if visited[ny][nx] == -1:
                        visited[ny][nx] = visited[y][x] + 1
                        q.append([nx, ny])

    bfs()
    return visited[m - 1][n - 1]