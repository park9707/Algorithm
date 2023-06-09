import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
chicken = []
house = []
answer = []
city = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

for combi in combinations(chicken, m):
    dist_sum = 0
    for h in house:
        dist = float("inf")
        hx, hy = h
        for c in combi:
            cx, cy = c
            dist = min(dist, abs(cx - hx) + abs(cy - hy))
        dist_sum += dist
    answer.append(dist_sum)

print(min(answer))
