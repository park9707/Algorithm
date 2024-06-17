import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [i for i in range(N + 1)]
for i in range(4, N + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    if i + i // 2 <= N:
        dp[i + i // 2] = dp[i] + 1

print('minigimbob' if dp[N] <= K else 'water')