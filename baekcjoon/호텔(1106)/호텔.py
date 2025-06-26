import sys
input = sys.stdin.readline

c, n = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
dp = [float('inf')] * (c + 101)
dp[0] = 0
ans = float('inf')

for i in range(c + 1):
    for cost, customer in city:
        dp[i + customer] = min(dp[i + customer], dp[i] + cost)

for i in range(c, c + 100):
    ans = min(ans, dp[i])

print(ans)