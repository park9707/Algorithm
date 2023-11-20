import sys
input = sys.stdin.readline

n = int(input())
weight = list(map(int, input().split()))
m = int(input())
bead = list(map(int, input().split()))
possible = {0}

for w in weight:
    temp = possible.copy()
    for p in temp:
        possible.add(w + p)
        possible.add(abs(w - p))

for b in bead:
    if b in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')