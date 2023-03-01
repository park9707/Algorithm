import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if dp[y][x] != 0:
        return dp[y][x]

    dp[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and graph[y][x] < graph[ny][nx]:
            dp[y][x] = max(dp[y][x], dfs(nx, ny) + 1)

    return dp[y][x]


ans = 0

for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(j, i))
print(ans)