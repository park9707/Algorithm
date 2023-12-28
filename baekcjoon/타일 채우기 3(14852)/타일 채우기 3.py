import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
dp_sum = [0 for _ in range(n+1)]
dp[0], dp[1] = 1, 2
dp_sum[0] = 1
dp_sum[1] = dp_sum[0] + dp[1]

if n <= 1:
    print(dp[n])
    exit(0)

for i in range(2, n+1):
    dp[i] = (dp_sum[i-1] * 2 + dp[i-2]) % 1000000007
    dp_sum[i] = (dp_sum[i-1] + dp[i]) % 1000000007

print(dp[-1] % 1000000007)
