import sys
input = sys.stdin.readline


def dfs(now, artist, cost):
    if dp[now][artist][cost] != 0:
        return dp[now][artist][cost]

    cnt = 0
    for i in range(1, n):
        if arr[artist][i] >= cost and now & (1 << i) <= 0:
            cnt = max(cnt, 1 + dfs(now | (1 << i), i, arr[artist][i]))
    dp[now][artist][cost] = cnt

    return cnt


n = int(input())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dp = [[[0] * 10 for _ in range(n)] for _ in range(1 << n)]
print(dfs(1, 0, 0) + 1)