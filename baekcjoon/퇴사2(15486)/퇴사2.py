import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 51)

for i in range(1, n + 1):
    t, p = map(int, input().split())
    dp[i] = max(dp[i], dp[i-1])
    next_i = i + t - 1
    dp[next_i] = max(dp[next_i], dp[i-1] + p)

print(dp[n])