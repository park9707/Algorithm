import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y, color):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if graph[nx][ny] == color:
                dfs(nx, ny, color)


n = int(input())

graph = []
visited = [[0] * n for _ in range(n)]
ans = 0
ans2 = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    graph.append(list(input().rstrip()))

for color in ['R', 'G', 'B']:
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j, color)
                ans += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * n for _ in range(n)]

for color in ['R', 'B']:
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j, color)
                ans2 += 1

print(ans, ans2)