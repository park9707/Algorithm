import sys
input = sys.stdin.readline

n, m = map(int, input().split())
investment = [[0 for _ in range(m + 1)]]

for _ in range(n):
    investment.append(list(map(int, input().split())))

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp_pos = [[[0 for _ in range(m + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if dp[i][j-1] <= investment[i][j]:
            dp[i][j] = investment[i][j]
            dp_pos[i][j][j] = i
        else:
            dp[i][j] = dp[i][j-1]
            dp_pos[i][j] = dp_pos[i][j-1].copy()

        for k in range(1, i + 1):
            if dp[i][j] < dp[k][j-1] + investment[i-k][j]:
                dp[i][j] = dp[k][j-1] + investment[i-k][j]
                dp_pos[i][j] = dp_pos[k][j-1].copy()
                dp_pos[i][j][j] = i-k

print(dp[-1][-1])
print(*dp_pos[-1][-1][1:])
