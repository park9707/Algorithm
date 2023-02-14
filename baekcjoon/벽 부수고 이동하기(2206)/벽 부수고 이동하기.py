from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        x, y, broken = q.popleft()

        if x == m-1 and y == n-1:
            return visited[y][x][broken]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx][broken]:
                if graph[ny][nx] == 0:
                    visited[ny][nx][broken] = visited[y][x][broken] + 1
                    q.append((nx, ny, broken))
                elif broken == 0:
                    visited[ny][nx][1] = visited[y][x][broken] + 1
                    q.append((nx, ny, 1))

    return -1


print(bfs())