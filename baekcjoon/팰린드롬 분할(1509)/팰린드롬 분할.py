import sys
input = sys.stdin.readline

s = input()
n = len(s)
dp = [2500] * n
dp[-1] = 0
is_p = [[False] * n for _ in range(n)]

for i in range(n):
    is_p[i][i] = True

for i in range(n-1):
    if s[i] == s[i+1]:
        is_p[i][i + 1] = True

for i in range(3, n + 1):
    for l in range(n - i + 1):
        r = l + i - 1
        if s[l] == s[r] and is_p[l + 1][r - 1]:
            is_p[l][r] = True

for r in range(n):
    for l in range(r + 1):
        if is_p[l][r]:
            dp[r] = min(dp[r], dp[l - 1] + 1)
        else:
            dp[r] = min(dp[r], dp[r - 1] + 1)

print(dp[-2])