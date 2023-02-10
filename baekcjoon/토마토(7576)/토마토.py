import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())

graph = [list(map(int, input().rstrip().split())) for i in range(n)]
cnt = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            q.append((x, y))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append((nx, ny))
for i in graph:
    if i.count(0) != 0:
        print(-1)
        break
else:
    print(graph[y][x]-1)