from collections import deque
from sys import stdin
input = stdin.readline

m, n = map(int, input().rstrip().split())

graph = [list(input().rstrip()) for _ in range(m)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = []


def bfs(x, y):
    visited = [[0] * n for _ in range(m)]
    visited[y][x] = 1
    q = deque([(x, y)])
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 'L':
                if not visited[ny][nx]:
                    visited[ny][nx] = visited[yy][xx] + 1
                    q.append((nx, ny))
    else:
        return visited[yy][xx] - 1


for y in range(m):
    for x in range(n):
        if graph[y][x] == 'L':
            answer.append(bfs(x, y))

print(max(answer))