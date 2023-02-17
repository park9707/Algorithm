from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for i in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = j, i


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0] * n for _ in range(n)]
    visited[y][x] = 1
    prey = []
    while q:
        i, j = q.popleft()

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if graph[ny][nx] < graph[y][x] and graph[ny][nx] != 0:
                    visited[ny][nx] = visited[j][i] + 1
                    prey.append((nx, ny, visited[ny][nx] - 1))

                elif graph[ny][nx] == graph[y][x] or graph[ny][nx] == 0:
                    visited[ny][nx] = visited[j][i] + 1
                    q.append((nx, ny))

    return sorted(prey, key=lambda a: (a[2], a[1], a[0]))


shark_size = [2, 0]
cnt = 0
while True:
    graph[y][x] = shark_size[0]
    prey = deque(bfs(x, y))

    if not prey:
        break

    xx, yy, dist = prey.popleft()
    cnt += dist
    shark_size[1] += 1

    if shark_size[0] == shark_size[1]:
        shark_size[0] += 1
        shark_size[1] = 0

    graph[y][x] = 0
    x, y = xx, yy

print(cnt)