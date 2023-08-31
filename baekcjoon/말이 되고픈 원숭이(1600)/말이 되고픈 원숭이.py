import sys, collections
input = sys.stdin.readline


def bfs():
    visited[0][0][0] = 1
    q = collections.deque()
    q.append([0, 0, 0])
    while q:
        x, y, cnt = q.popleft()

        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][cnt] and not board[nx][ny]:
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                q.append([nx, ny, cnt])
                if nx == h - 1 and ny == w - 1:
                    return visited[x][y][cnt]

        if cnt < k:
            for dx, dy in horse_move:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][cnt + 1] and not board[nx][ny]:
                    visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                    q.append([nx, ny, cnt + 1])
                    if nx == h - 1 and ny == w - 1:
                        return visited[x][y][cnt]
    return -1


k = int(input().rstrip())
w, h = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(h)]

move = ((0, 1), (0, -1), (1, 0), (-1, 0))
horse_move = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2))
visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]

if w == 1 and h == 1:
    print(0)
else:
    print(bfs())
