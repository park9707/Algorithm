import sys
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    parents[b] = a


while True:
    m, n = map(int, input().split())
    if m == 0:
        break
    road = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        road.append([c, a, b])
    parents = [i for i in range(m)]
    ans = 0
    road.sort()

    for i in range(n):
        c, a, b = road[i]
        if find(a) != find(b):
            union(parents[a], parents[b])
        else:
            ans += c

    print(ans)