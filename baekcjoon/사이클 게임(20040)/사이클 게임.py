import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
        return parents[x]
    return x


def union(a, b):
    x = find(a)
    y = find(b)
    if x < y:
        parents[x] = y
    elif y < x:
        parents[y] = x
    else:
        return True
    return False


n, m = map(int, input().split())
parents = [i for i in range(n)]

for i in range(1, m + 1):
    a, b = map(int, input().split())
    if union(a, b):
        print(i)
        break
else:
    print(0)