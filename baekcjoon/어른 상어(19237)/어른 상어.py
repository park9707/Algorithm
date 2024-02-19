import sys, collections
input = sys.stdin.readline

N, M, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))
move = ((), (-1, 0), (1, 0), (0, -1), (0, 1))
priority = [[]]
for _ in range(M):
    temp = [[]]
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priority.append(temp)

q = [[] for _ in range(M)]
visited = [[[-1, 0] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            num = board[i][j]
            q[num - 1] = [num, i, j, direction[num - 1]]
q = collections.deque(q)

for t in range(1000):
    new_board = [[0] * N for _ in range(N)]
    for _ in range(len(q)):
        num, x, y, d = q.popleft()
        visited[x][y] = [t + k, num]
        next_xy = []
        for j in priority[num][d]:
            dx, dy = move[j]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny]:
                    continue
                elif visited[nx][ny][0] <= t:
                    if new_board[nx][ny] == 0:
                        new_board[nx][ny] = num
                        q.append([num, nx, ny, j])
                    break
                elif visited[nx][ny][1] == num and not next_xy:
                    if new_board[nx][ny] != 0:
                        break
                    next_xy = [nx, ny, j]
        else:
            if next_xy:
                nx, ny, j = next_xy
                new_board[nx][ny] = num
                q.append([num, nx, ny, j])

    if q[0][0] != 1:
        print(-1)
        exit()
    elif len(q) == 1:
        print(t + 1)
        exit()

    board = new_board

print(-1)