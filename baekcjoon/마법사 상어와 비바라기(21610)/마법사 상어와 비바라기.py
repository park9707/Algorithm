import sys
input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move = [[], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
cloud = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]
moved_cloud = []
visited = [[-1] * N for _ in range(N)]

for n in range(M):
    d, s = map(int, input().split())
    dx, dy = move[d][0] * s % N, move[d][1] * s % N

    # 구름 이동
    for _ in range(len(cloud)):
        x, y = cloud.pop()
        nx = (N + x + dx) % N
        ny = (N + y + dy) % N
        board[nx][ny] += 1
        moved_cloud.append([nx, ny])
        visited[nx][ny] = n

    # 대각선 확인 후 물이 있는 바구니 수 만큼 물의 양 증가
    for _ in range(len(moved_cloud)):
        x, y = moved_cloud.pop()
        for i in [2, 4, 6, 8]:
            dx, dy = move[i]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny]:
                board[x][y] += 1

    # 이전에 구름이 있었던 곳이 아니고, 물의 양이 2 이상인 구름 생성
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and visited[i][j] != n:
                cloud.append([i, j])
                board[i][j] -= 2

print(sum([sum(board[i]) for i in range(N)]))
