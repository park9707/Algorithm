from collections import deque
from sys import stdin
input = stdin.readline

n, l, r = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0


def bfs(x, y):
    global visited, graph
    visited[y][x] = True
    q = deque([(x, y)])
    cnt = 1
    v = graph[y][x]
    d = [(x, y)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if l <= abs(graph[y][x] - graph[ny][nx]) <= r:
                    cnt += 1
                    v += graph[ny][nx]
                    d.append((nx, ny))
                    visited[ny][nx] = True
                    q.append((nx, ny))

    if not d == [(x, y)]:
        b = v // cnt
        for i, j in d:
            graph[j][i] = b
    return cnt


while True:
    visited = [[False] * n for _ in range(n)]
    a = 1
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                a = max(a, bfs(x, y))
    if a == 1:
        print(answer)
        break
    else:
        answer += 1