import sys, copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n, m, d = map(int, input().split())
answer = 0
enemy = 0
move = [[0, -1], [-1, 0], [0, 1]]
maps = []
for _ in range(n):
    e = list(map(int, input().split()))
    enemy += e.count(1)
    maps.append(e)


def bfs(ix, iy, d):
    q = deque([[ix, iy, d]])
    while q:
        x, y, dist = q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ix < nx or ny < 0 or m-1 < ny:
                continue

            if tmp[nx][ny] == 1:
                return nx, ny
            else:
                if dist > 1:
                    q.append([nx, ny, dist - 1])
    return False


for archers in combinations(range(m), 3):
    cnt = 0
    no_remove = 0
    tmp = copy.deepcopy(maps)
    for wave in range(n-1, -1, -1):
        remove = set()
        for archer in archers:
            if tmp[wave][archer] == 1:
                remove.add((wave, archer))
            elif d > 1:
                answer = bfs(wave, archer, d - 1)
                if answer:
                    remove.add(answer)

        for x, y in remove:
            tmp[x][y] = 0
        no_remove += tmp[wave].count(1)
        cnt += len(remove)

        if no_remove + cnt == enemy:
            break
    answer = max(answer, cnt)
    if answer == enemy:
        break

print(answer)
