from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(100000)

input = stdin.readline

n = int(input().rstrip())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
max_num = 0
result = 1
for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))
    tmp = max(graph[i])
    max_num = max(max_num, tmp)


def dfs(x, y, num):
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= n or nx < 0 or ny >= n or ny < 0:
            continue

        if not visited[ny][nx] and graph[ny][nx] > num:
            dfs(nx, ny, num)


for num in range(1, max_num+1):
    cnt = 0
    visited = [[False] * (n+1) for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[y][x] and graph[y][x] > num:
                dfs(x, y, num)
                cnt += 1

    result = max(result, cnt)

stdout.write(str(result))