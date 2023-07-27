from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10000)

input = stdin.readline

t = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = []


def dfs(y, x):
    if x < 0 or x >= m or y < 0 or y >= n:
        return

    if graph[y][x] == 1:
        graph[y][x] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(ny, nx)


for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                dfs(y, x)
                cnt += 1

    stdout.write(str(cnt)+"\n")