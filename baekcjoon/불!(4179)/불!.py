import sys, collections
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
maps = []
visited = [[False] * c for _ in range(r)]
q = collections.deque()
fire_q = collections.deque()

for i in range(r):
    maps.append(list(input().rstrip()))
    for j in range(c):
        if maps[i][j] == 'J':
            maps[i][j] = '.'
            q.append([i, j, 0])
            visited[i][j] = True
        elif maps[i][j] == 'F':
            fire_q.append([i, j, 0])
            visited[i][j] = True

n = 0
move = ((0, 1), (0, -1), (1, 0), (-1, 0))
answer = 'IMPOSSIBLE'

while q:
    n += 1
    while q and q[0][2] < n:
        x, y, time = q.popleft()
        if maps[x][y] != '.':
            continue
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if maps[nx][ny] == '.' and not visited[nx][ny]:
                    q.append([nx, ny, time + 1])
                    visited[nx][ny] = True
            else:
                answer = time + 1
                break
        else:
            continue
        break

    else:
        while fire_q and fire_q[0][2] < n:
            x, y, time = fire_q.popleft()
            for dx, dy in move:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    if maps[nx][ny] == '.':
                        fire_q.append([nx, ny, time + 1])
                        maps[nx][ny] = '#'
        continue
    break

print(answer)
