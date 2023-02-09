m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1] * n for _ in range(m)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    if visited[y][x] != -1:
        return visited[y][x]

    visited[y][x] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[y][x] > graph[ny][nx]:
                visited[y][x] += dfs(nx, ny)
    return visited[y][x]


print(dfs(0, 0))