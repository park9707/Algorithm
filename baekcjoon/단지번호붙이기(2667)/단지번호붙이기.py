from sys import stdin, stdout

input = stdin.readline

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().strip())))

cnt = 0
answer = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    global cnt
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            answer.append(cnt)

answer.sort()

stdout.write(str(len(answer)) + "\n")
for i in answer:
    stdout.write(str(i)+"\n")
