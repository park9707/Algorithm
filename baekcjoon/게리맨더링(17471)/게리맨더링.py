import sys, itertools, collections
input = sys.stdin.readline

n = int(input().rstrip())
people = [0] + list(map(int, input().rstrip().split()))
wire = [[]]

for i in range(n):
    temp = list(map(int, input().rstrip().split()))
    wire.append(temp[1:])


def is_connected(group):
    visited = [True] * (n + 1)
    for g in group[1:]:
        visited[g] = False
    start = group[0]
    q = collections.deque([start])
    while q:
        x = q.popleft()
        for w in wire[x]:
            if not visited[w]:
                q.append(w)
                visited[w] = True
    if False in visited:
        return False
    else:
        return True


area = set(i for i in range(1, n + 1))
answer = []
for i in range(1, n // 2 + 1):
    combi = list(itertools.combinations(area, i))
    for a in combi:
        b = list(area.difference(a))

        if is_connected(a) and is_connected(b):
            answer.append(abs(sum(people[num] for num in a) - sum(people[num] for num in b)))

print(min(answer) if answer else -1)
