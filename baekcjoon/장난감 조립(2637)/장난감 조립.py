import sys, collections
input = sys.stdin.readline

n = int(input())
m = int(input())
parts = [[0] * (n + 1) for _ in range(n + 1)]
needs = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
q = collections.deque()

for _ in range(m):
    x, y, k = map(int, input().split())
    needs[y].append([x, k])
    degree[x] += 1

for i in range(1, n):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    for next_num, next_needs in needs[now]:
        if parts[now].count(0) == n + 1:
            parts[next_num][now] += next_needs
        else:
            for i in range(1, n):
                parts[next_num][i] += parts[now][i] * next_needs

        degree[next_num] -= 1
        if degree[next_num] == 0:
            q.append(next_num)

for i, v in enumerate(parts[n]):
    if v > 0:
        print(i, v)