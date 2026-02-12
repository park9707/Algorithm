import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 31
dp[0], dp[2] = 1, 3

for i in range(4, n + 1, 2):
    dp[i] = dp[i - 2] * 4 - dp[i - 4]

print(dp[n])