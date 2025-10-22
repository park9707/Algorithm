import sys
input = sys.stdin.readline

g = int(input())
pre, now = 1, 1
ans = []
limit = min(g, 50000)

while pre < limit:
    diff = (now * now) - (pre * pre)
    if g == diff:
        ans.append(now)
        pre += 1
        now += 1
    elif g < diff:
        pre += 1
    else:
        now += 1

if ans:
    for i in ans:
        print(i)
else:
    print(-1)