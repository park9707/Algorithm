import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memories = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
total_cost = sum(cost)

dp = [[0] * (total_cost + 1) for _ in range(n + 1)]
ans = float('inf')

for i in range(1, n + 1):
    for j in range(total_cost + 1):
        if j < cost[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], memories[i] + dp[i-1][j-cost[i]])

        if m <= dp[i][j]:
            ans = min(ans, j)

print(ans)