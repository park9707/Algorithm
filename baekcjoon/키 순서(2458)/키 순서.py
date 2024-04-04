import sys
input = sys.stdin.readline


def dfs(now, nxt):
    for j in arr[nxt]:
        if not p[now][j]:
            p[now][j] = 1
            p[j][now] = 1
            dfs(now, j)


N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

p = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    p[i][i] = 1
    dfs(i, i)

print(sum(1 if sum(p[i]) == N else 0 for i in range(1, N + 1)))
