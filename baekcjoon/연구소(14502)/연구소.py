from collections import deque
from copy import deepcopy
from sys import stdin

input = stdin.readline

n, m = map(int, input().rstrip().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    tmp_graph = deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                q.append((j, i))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if tmp_graph[ny][nx] == 0:
                    tmp_graph[ny][nx] = 2
                    q.append((nx, ny))

    cnt = 0

    for i in tmp_graph:
        cnt += i.count(0)

    global answer
    result = max(result, cnt)

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0


graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
answer = 0
make_wall(0)

print(answer)