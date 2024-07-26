import sys, collections
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    if b < a:
        parents[a] = b
    else:
        parents[b] = a


r, c = map(int, input().split())
board = []
swan = []
move = ((0, 1), (1, 0), (0, -1), (-1, 0))
for i in range(r):
    temp = list(input().rstrip())
    for j in range(c):
        if temp[j] == 'L':
            swan.append([i, j])
            temp[j] = '.'
    board.append(temp)

visited = [[0] * c for _ in range(r)]
parents = [0]
p = 1
next_q = []
for i in range(r):
    for j in range(c):
        if board[i][j] == '.' and not visited[i][j]:
            q = collections.deque([[i, j]])
            visited[i][j] = p
            parents.append(p)
            while q:
                x, y = q.popleft()
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                        if board[nx][ny] == '.':
                            q.append([nx, ny])
                        else:
                            next_q.append([nx, ny])
                        visited[nx][ny] = p
            p += 1

x1, y1 = swan[0]
x2, y2 = swan[1]
swan1, swan2 = visited[x1][y1], visited[x2][y2]
q = collections.deque(next_q)

for i in range(1, 1500):
    for x, y in q:
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny]:
                if visited[nx][ny] != visited[x][y]:
                    a = find(visited[x][y])
                    b = find(visited[nx][ny])
                    if a != b:
                        union(a, b)

    if find(parents[swan1]) == find(parents[swan2]):
        print(i)
        exit()

    for _ in range(len(q)):
        x, y = q.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 'X':
                if not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y]
