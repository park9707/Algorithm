import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(num):
    visited[num] = True
    if not tree[num]:
        dp[num][1] = 1
        dp[num][0] = 0
        return

    for i in tree[num]:
        if visited[i] == 0:
            dfs(i)
            dp[num][1] += min(dp[i][0], dp[i][1])
            dp[num][0] += dp[i][1]
    dp[num][1] += 1


dfs(1)
print(min(dp[1][0], dp[1][1]))