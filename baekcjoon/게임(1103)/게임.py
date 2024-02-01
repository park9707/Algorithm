import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]
move = ((0, -1), (-1, 0), (0, 1), (1, 0))
visited[0][0] = True
dp[0][0] = 1


def dfs(x, y):
    d = int(board[x][y])
    cnt = dp[x][y]
    for dx, dy in move:
        nx = x + (dx * d)
        ny = y + (dy * d)
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 'H' and cnt >= dp[nx][ny]:
            if not visited[nx][ny]:
                dp[nx][ny] = cnt + 1
                visited[nx][ny] = True
                dfs(nx, ny)
                visited[nx][ny] = False
            else:
                print(-1)
                exit(0)


dfs(0, 0)
print(max(map(max, [dp[i] for i in range(N)])))
