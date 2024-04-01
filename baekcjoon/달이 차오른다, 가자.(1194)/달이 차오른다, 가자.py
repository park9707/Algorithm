import sys, collections
input = sys.stdin.readline


N, M = map(int, input().split())
maze = []
x, y = -1, -1
for i in range(N):
    temp = list(input().rstrip())
    for j in range(M):
        if x != -1:
            break
        elif temp[j] == '0':
            x, y = i, j
            temp[j] = '.'
    maze.append(temp)
move = ((1, 0), (0, 1), (-1, 0), (0, -1))
q = collections.deque([[x, y, 0, 0, 0, 0, 0, 0]])
visited = [[[[[[[[False for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)]
              for _ in range(2)] for _ in range(2)] for _ in range(M)] for _ in range(N)]
visited[x][y][0][0][0][0][0][0] = True
dic = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7}
ans = 0
while q:
    ans += 1
    for i in range(len(q)):
        x, y, a, b, c, d, e, f = q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == '#' or visited[nx][ny][a][b][c][d][e][f]:
                    continue

                next_ = [nx, ny, a, b, c, d, e, f]

                if maze[nx][ny] == '1':
                    print(ans)
                    exit()
                elif maze[nx][ny] == '.':
                    visited[nx][ny][a][b][c][d][e][f] = True
                elif maze[nx][ny].isupper():
                    word = maze[nx][ny].lower()
                    if not next_[dic[word]]:
                        continue
                    visited[nx][ny][a][b][c][d][e][f] = True
                elif maze[nx][ny].islower():
                    idx = dic[maze[nx][ny]]
                    next_[idx] = 1
                    visited[nx][ny][next_[2]][next_[3]][next_[4]][next_[5]][next_[6]][next_[7]] = True

                q.append(next_)

print(-1)