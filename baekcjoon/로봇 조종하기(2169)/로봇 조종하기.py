import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]

for j in range(1, m):
    dp[0][j] += dp[0][j-1]

for i in range(1, n):
    tmp1 = [dp[i-1][0] + dp[i][0]]
    tmp2 = [dp[i-1][-1] + dp[i][-1]]

    for j in range(1, m):
        tmp1.append(max(tmp1[-1] + dp[i][j], dp[i-1][j] + dp[i][j]))
        tmp2.append(max(tmp2[-1] + dp[i][-j-1], dp[i-1][-j-1] + dp[i][-j-1]))

    for k in range(m):
        dp[i][k] = max(tmp1[k], tmp2[m-k-1])

print(dp[-1][-1])