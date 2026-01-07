import sys
input = sys.stdin.readline


def bf():
    dist = [10000 * 500] * (n + 1)
    dist[edges[0][0]] = 0
    for i in range(n):
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == n - 1:
                    return 'YES'
    return 'NO'


for _ in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append([a, b, c])
        edges.append([b, a, c])
    for _ in range(w):
        a, b, c = map(int, input().split())
        edges.append([a, b, -c])

    print(bf())