import sys, heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(i, depth):
    heapq.heappush(q, (depth, i))
    for j in subordinate[i]:
        dfs(j, depth + 1)


n, m = map(int, input().split())
subordinate = [[] for _ in range(n + 1)]
superior = list(map(int, input().split()))

for i, s in enumerate(superior[1:], 2):
    subordinate[s].append(i)

q = []
ans = [0] * (n + 1)

for _ in range(m):
    i, w = map(int, input().split())
    ans[i] += w

dfs(1, 0)

while q:
    _, i = heapq.heappop(q)
    value = ans[i]
    for j in subordinate[i]:
        ans[j] += value

print(*ans[1:])
