import sys
input = sys.stdin.readline

n = int(input())
t = []
ans = 0
room = 0
for _ in range(n):
    a, b = map(int, input().split())
    t.append([a, 1])
    t.append([b, -1])

t.sort()

for i in range(n * 2 - 1):
    _, se = t[i]
    room += se
    ans = max(ans, room)
    if n * 2 - ans < i:
        break

print(ans)