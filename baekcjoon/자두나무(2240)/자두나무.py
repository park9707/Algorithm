import sys
input = sys.stdin.readline

t, w = map(int, input().split())
dp = [[0] * (w + 1) for _ in range(t + 1)]

for i in range(1, t + 1):
    n = int(input())
    dp[i][0] = dp[i - 1][0] + (n % 2)
    for j in range(1, w + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
        if n - 1 == j % 2:
            dp[i][j] += 1

print(max(dp[-1]))
