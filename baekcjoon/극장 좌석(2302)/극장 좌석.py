import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vips = []
for _ in range(m):
    vips.append(int(input()))
vips.append(n + 1)

dp = [1, 1, 2]
for i in range(3, n - m + 1):
    dp.append(dp[i-1] + dp[i-2])

ans = 1
idx = 1
for vip in vips:
    ans *= dp[vip - idx]
    idx = vip + 1

print(ans)