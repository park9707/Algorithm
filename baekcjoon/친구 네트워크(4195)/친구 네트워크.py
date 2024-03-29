import sys
input = sys.stdin.readline
print = sys.stdout.write


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    if x == y:
        return
    friends[x] += friends[y]
    parents[y] = x


def check(x):
    if parents.get(x) is None:
        parents[x] = x
        friends[x] = 1
        return x
    else:
        return find(x)


t = int(input().rstrip())

for _ in range(t):
    f = int(input().rstrip())
    parents = dict()
    friends = dict()
    for _ in range(f):
        a, b = input().split()

        a_parents = check(a)
        b_parents = check(b)

        union(a_parents, b_parents)

        print(str(friends[a_parents]) + '\n')
