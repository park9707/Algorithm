import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, k = map(int, input().split())
nourishment = [list(map(int, input().split())) for _ in range(n)]
maps = [[5] * n for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
move = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for _ in range(m):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

def eat():
    breed = defaultdict(int)
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                trees[i][j].sort()
                food = maps[i][j]
                stack = []
                died = 0
                for idx in range(len(trees[i][j])):
                    a = trees[i][j][idx]
                    if food - a >= 0:
                        food -= a
                        a += 1
                        stack.append(a)
                        if a % 5 == 0:
                            breed[i, j] += 1
                    else:
                        died += a // 2
                trees[i][j] = stack
                maps[i][j] = food + died
    return breed

def breeding(breed):
    for key, value in breed.items():
        x, y = key
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                for _ in range(value):
                    trees[nx][ny].append(1)

for _ in range(k):
    breed = eat()
    breeding(breed)
    maps = [[maps[i][j] + nourishment[i][j] for j in range(n)] for i in range(n)]

print(sum(len(v) for tree in trees for v in tree))
