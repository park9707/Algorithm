import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().rstrip().split())

graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
max_z = n*m
z_cnt = 0
answer = 0

for i in graph:
    z_cnt += i.count(0)

def check(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= m and 0 <= ny <= n:
            if tmp_graph[ny][nx] <= 0:
                cnt += 1
    graph[y][x] -= cnt

    if graph[y][x] <= 0:
        global z_cnt
        z_cnt += 1


def dfs(x, y):
    visited[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 < nx < m and 0 < ny < n:
            if not visited[ny][nx] and graph[ny][nx] > 0:
                dfs(nx, ny)


while max_z != z_cnt:
    tmp_z = z_cnt
    tmp_graph = copy.deepcopy(graph)
    for x in range(1, m):
        for y in range(1, n):
            if tmp_graph[y][x] > 0:
                check(x, y)
    answer += 1
    if tmp_z == z_cnt:
        continue

    visited = [[False] * (m + 1) for _ in range(n)]
    d = 0
    for x in range(1, m):
        for y in range(1, n):
            if not visited[y][x] and graph[y][x] > 0:
                dfs(x, y)
                d += 1
    if d > 1:
        print(answer)
        break
else:
    print(0)