import sys
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


n = int(input())
parents = list(range(n + 1))
ans = []
for _ in range(n - 2):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, n + 1):
    if parents[i] == i:
        ans.append(i)

print(*ans)
