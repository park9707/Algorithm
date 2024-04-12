import sys, itertools, copy
input = sys.stdin.readline

N, M = map(int, input().split())
virus = []
v = [[0] * N for _ in range(N)]
move = ((1, 0), (0, 1), (-1, 0), (0, -1))
ans = float('inf')
cnt = 0
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 2:
            virus.append([i, j])
            v[i][j] = -2
        elif temp[j] == 1:
            v[i][j] = 1
        else:
            cnt += 1

if cnt == 0:
    print(0)
    exit()

for combi in list(itertools.combinations(range(len(virus)), M)):
    arr = []
    visited = copy.deepcopy(v)
    a = cnt
    for i in combi:
        x, y = virus[i]
        arr.append([x, y])
        visited[x][y] = 1
    for i in range(1, N * N):
        new_arr = []
        for j in range(len(arr)):
            x, y = arr[j]
            for dx, dy in move:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] < 1:
                    new_arr.append([nx, ny])
                    if visited[nx][ny] == 0:
                        a -= 1
                    visited[nx][ny] = 1

        if not new_arr or a == 0:
            break

        arr = new_arr

    if a == 0:
        ans = min(ans, i)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
