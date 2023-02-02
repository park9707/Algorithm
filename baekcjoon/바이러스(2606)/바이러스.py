from sys import stdin,stdout
from collections import defaultdict

input = stdin.readline

cnt = 0
def dfs(line, v, visited):
    visited[v] = True
    global cnt
    cnt += 1

    for i in line[v]:
        if not visited[i]:
            dfs(line, i, visited)

com = int(input())
c = int(input())
line = defaultdict(list)


for _ in range(c):
    a, b = map(int, input().split())
    line[a].append(b)
    line[b].append(a)
visited = [False] * (com+1)
dfs(line, 1, visited)

stdout.write(str(cnt-1))