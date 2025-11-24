import sys
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    parents[b] = a


g = int(input())
p = int(input())
parents = list(map(int, range(g + 1)))
ans = 0
for _ in range(p):
    airplane = int(input())
    gate = find(airplane)
    if gate == 0:
        break
    union(gate - 1, gate)
    ans += 1

print(ans)