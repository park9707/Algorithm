import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
students = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
ans = []
for _ in range(m):
    a, b = map(int, input().split())
    students[a].append(b)
    indegree[b] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    ans.append(now)
    for student in students[now]:
        indegree[student] -= 1
        if indegree[student] == 0:
            q.append(student)

print(*ans)