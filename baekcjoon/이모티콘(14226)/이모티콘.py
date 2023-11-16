import sys, collections
input = sys.stdin.readline

s = int(input())
limit = min(s + min((s // 4), 1), 1500) + 1
dp = [[0] * limit for _ in range(limit)]
q = collections.deque([[1, 0]])

while q:
    x, y = q.popleft()
    t = dp[x][y] + 1
    if x + y < limit and dp[x + y][y] == 0:
        dp[x + y][y] = t
        q.append([x + y, y])
        if x + y == s:
            break
    if 1 < x - 1 and dp[x - 1][y] == 0:
        dp[x - 1][y] = t
        q.append([x - 1, y])
        if x - 1 == s:
            break
    if dp[x][x] == 0:
        dp[x][x] = t
        q.append([x, x])

print(t)