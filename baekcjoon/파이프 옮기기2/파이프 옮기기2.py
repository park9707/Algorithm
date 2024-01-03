import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for j in range(2, n):
    if board[0][j] == 1:
        break
    dp[0][j][0] = 1

for i in range(1, n):
    for j in range(2, n):
        if board[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            dp[i][j][2] = dp[i-1][j][2] + dp[i-1][j][1]
            if board[i][j-1] == 0 and board[i-1][j] == 0:
                dp[i][j][1] = sum(dp[i-1][j-1])

print(sum(dp[-1][-1]))