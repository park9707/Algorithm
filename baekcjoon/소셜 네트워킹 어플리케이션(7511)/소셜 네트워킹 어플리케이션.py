import sys
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a <= b:
        parents[b] = a
    else:
        parents[a] = b


t = int(input())
for i in range(t):
    n = int(input())
    parents = [p for p in range(n)]
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)

    m = int(input())
    print(f"Scenario {i + 1}:")
    for _ in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b):
            print(1)
        else:
            print(0)
    print()
