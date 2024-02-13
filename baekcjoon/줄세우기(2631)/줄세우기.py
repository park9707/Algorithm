import sys
input = sys.stdin.readline

N = int(input())
dp = [1] * N
num = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
