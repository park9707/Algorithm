import sys, collections
input = sys.stdin.readline

n = int(input())
q = collections.deque()
indegree = [0] * (n + 1)
time = [0] * (n + 1)
dp = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    tower = list(map(int, input().split()))
    time[i] = tower[0]
    for j in tower[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = time[i]

while q:
    now = q.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        dp[i] = max(dp[i], dp[now] + time[i])
        if indegree[i] == 0:
            q.append(i)

for i in range(1, n + 1):
    print(dp[i])
