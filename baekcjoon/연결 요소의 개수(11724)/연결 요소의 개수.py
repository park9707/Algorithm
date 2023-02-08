from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict

setrecursionlimit(10000)

input = stdin.readline

n, m = map(int, input().split())
visited = [False] * (n+1)
graph = defaultdict(list)
cnt = 0

for i in range(1, m+1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        cnt += 1

stdout.write(str(cnt))