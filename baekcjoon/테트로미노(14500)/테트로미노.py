import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_num = max(map(max, board))


def dfs(x, y, depth, v):
    global cnt
    # 현재 값에서 남은 깊이만큼 제일 높은 값을 곱해도 현재 ans보다 작으면 실행하지 않음
    if v + (4 - depth) * max_num < ans:
        return
    if depth == 4:
        ans = max(ans, v)
        return

    for dx, dy in move:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                if depth == 2:
                    visited[nx][ny] = True
                    dfs(x, y, depth + 1, v + board[nx][ny])
                    visited[nx][ny] = False
                visited[nx][ny] = True
                dfs(nx, ny, depth + 1, v + board[nx][ny])
                visited[nx][ny] = False


cnt = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

print(cnt)
