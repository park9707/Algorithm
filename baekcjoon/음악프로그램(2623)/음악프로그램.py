import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    temp = list(map(int, input().split()))
    for i in range(1, temp[0]):
        indegree[temp[i + 1]] += 1
        graph[temp[i]].append(temp[i + 1])

q = deque()
ans = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    singer = q.popleft()
    ans.append(singer)
    for i in graph[singer]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(ans) == n:
    for a in ans:
        print(a)
else:
    print(0)