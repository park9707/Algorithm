import sys, collections

input = sys.stdin.readline

n = int(input())
scv = sorted(list(map(int, input().split())), reverse=True)
scv += [0] * (3 - len(scv))
visited = [[[False] * max(scv[2], 1) for _ in range(max(scv[1], 1))] for _ in range(scv[0])]
damage = ((9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9))
q = collections.deque([[0, *scv]])

while q:
    num, a, b, c = q.popleft()
    for i, j, k in damage:
        d = max(a - i, 0)
        e = max(b - j, 0)
        f = max(c - k, 0)

        if d + e + f == 0:
            print(num + 1)
            exit(0)

        if not visited[d][e][f]:
            visited[d][e][f] = True
            q.append([num + 1, d, e, f])
