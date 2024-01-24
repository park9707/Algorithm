import sys
input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
arr = [[[] for _ in range(N)] for _ in range(N)]
horse = {}
move = ((0, 1), (0, -1), (-1, 0), (1, 0))
toggle = {0: 1, 1: 0, 2: 3, 3: 2}

for i in range(K):
    a, b, d = map(int, input().split())
    horse[i] = [a - 1, b - 1, d - 1]
    arr[a-1][b-1].append(i)

for t in range(1, 1001):
    for i in range(K):
        x, y, d = horse[i]
        dx, dy = move[d]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
            d = toggle[d]
            dx, dy = move[d]
            nx, ny = x + dx, y + dy
            horse[i][2] = d

            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
                continue

        idx = arr[x][y].index(i)
        temp = []

        for j in range(len(arr[x][y]), idx, -1):
            num = arr[x][y].pop()
            temp.append(num)
            horse[num] = [nx, ny, horse[num][2]]

        if board[nx][ny] == 0:
            arr[nx][ny].extend(temp[::-1])
        elif board[nx][ny] == 1:
            arr[nx][ny].extend(temp)

        if len(arr[nx][ny]) >= 4:
            print(t)
            exit(0)
print(-1)