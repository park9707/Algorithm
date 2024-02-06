import sys, bisect
input = sys.stdin.readline

N = int(input())
t = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = [0] * N
dp[0] = c[0]

for i in range(1, N):
    if t[i] == b[i]:
        dp[i] = max(dp[i-1], c[i])
        continue

    left = bisect.bisect_left(t, t[i] - b[i])
    dp[i] = max(dp[i-1], dp[left-1] + c[i])

print(dp[-1])
