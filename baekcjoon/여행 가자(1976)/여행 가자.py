import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
parents = [i for i in range(n)]
plan = list(map(int, input().rstrip().split()))


def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i, j)

ans = "YES"
for i in range(1, m):
    if parents[plan[i] - 1] != parents[plan[0] - 1]:
        ans = "NO"
        break

print(ans)