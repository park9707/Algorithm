import sys, collections
input = sys.stdin.readline

m, n, h = map(int, input().rstrip().split())
tomato = []
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
q = collections.deque()

for i in range(h):
    row = []
    for j in range(n):
        tmp = list(map(int, input().rstrip().split()))
        for k in range(m):
            if tmp[k] == 1:
                q.append([0, i, j, k])
                visited[i][j][k] = True
            elif tmp[k] == -1:
                visited[i][j][k] = True
        row.append(tmp)
    tomato.append(row)

move = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
cnt = 0

while q:
    cnt, z, x, y = q.popleft()
    for dz, dx, dy in move:
        nz = z + dz
        nx = x + dx
        ny = y + dy

        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
            if not visited[nz][nx][ny]:
                visited[nz][nx][ny] = True
                q.append([cnt + 1, nz, nx, ny])
                tomato[nz][nx][ny] = 1

for i in range(h):
    for j in range(n):
        if 0 in tomato[i][j]:
            break
    else:
        continue
    print(-1)
    break
else:
    print(cnt)