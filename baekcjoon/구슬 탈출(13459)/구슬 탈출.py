import sys, collections
input = sys.stdin.readline


def tilt(x, y, dx, dy):
    cnt = 0
    while True:
        x += dx
        y += dy

        if board[x][y] == '#':
            return [x-dx, y-dy, cnt]

        elif board[x][y] == 'O':
            return [-1, -1, -1]

        cnt += 1


N, M = map(int, input().split())
board = []
bx = by = rx = ry = 0
for i in range(N):
    temp = list(input())
    for j in range(M):
        if temp[j] == 'R':
            rx, ry = i, j
        elif temp[j] == 'B':
            bx, by = i, j
    board.append(temp)

q = collections.deque([[rx, ry, bx, by]])
visited = {(rx, ry, bx, by): True}
move = ((1, 0), (0, 1), (-1, 0), (0, -1))

for _ in range(10):
    for _ in range(len(q)):
        rx, ry, bx, by = q.popleft()
        for dx, dy in move:
            nbx, nby, bc = tilt(bx, by, dx, dy)
            if nbx == -1:
                continue

            nrx, nry, rc = tilt(rx, ry, dx, dy)
            if nrx == -1:
                print(1)
                exit()
            elif nrx == nbx and nry == nby:
                if rc < bc:
                    nbx -= dx
                    nby -= dy
                elif rc > bc:
                    nrx -= dx
                    nry -= dy

            if not visited.get((nrx, nry, nbx, nby), False):
                visited[nrx, nry, nbx, nby] = True
                q.append([nrx, nry, nbx, nby])
print(0)