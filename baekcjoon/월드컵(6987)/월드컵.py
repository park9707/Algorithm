import sys
from itertools import combinations
input = sys.stdin.readline


def dfs(r):
    global cnt
    if r == 15:
        cnt = 1
        for a in arr:
            if a.count(0) != 3:
                cnt = 0
                break
        return

    g1, g2 = games[r]
    for w, l in ((2, 0), (1, 1), (0, 2)):
        if arr[g1][w] > 0 and arr[g2][l] > 0:
            arr[g1][w] -= 1
            arr[g2][l] -= 1
            dfs(r + 1)
            arr[g1][w] += 1
            arr[g2][l] += 1


games = list(combinations(range(6), 2))

for _ in range(4):
    result = list(map(int, input().split()))
    arr = [result[i:i+3] for i in range(0, 16, 3)]
    cnt = 0
    dfs(0)
    print(cnt)
