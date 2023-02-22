from sys import stdin
input = stdin.readline

n = int(input().rstrip())

wines = [0] + [int(input().rstrip()) for _ in range(n)]
dp = [0, wines[1]]
if n > 1:
    dp.append(wines[1] + wines[2])
for i in range(3, n+1):
    dp.append(max(dp[i-3] + wines[i-1] + wines[i], dp[i-2] + wines[i], dp[i-1]))

print(dp[n])