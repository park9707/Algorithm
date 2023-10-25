import sys
input = sys.stdin.readline


def find(x):
    if x == parents[x]:
        return x
    return find(parents[x])


def union(a, b):
    a = find(a)
    b = find(b)

    if a <= b:
        parents[b] = a
    else:
        parents[a] = b


n, m = map(int, input().split())
temp = list(map(int, input().split()))
if len(temp) == 1:
    print(m)
    exit(0)
parents = [i for i in range(n + 1)]

for i in temp[1:]:
    parents[i] = 0

parties = []
for _ in range(m):
    party = list(map(int, input().split()))[1:]
    f_num = party[0]
    for num in party[1:]:
        union(f_num, num)
    parties.append(party)

ans = 0
for p in parties:
    for num in p:
        if find(num) == 0:
            break
    else:
        ans += 1

print(ans)