import sys
input = sys.stdin.readline

n = int(input())
work = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: [x[0], x[1]])
m = work[-1][0] + 1
k = 0
ans = 0
required_k = [0] * m
for t, l in work:
    required_k[t] = l

for i in range(m - 2, 0, -1):
    required_k[i] = max(required_k[i], required_k[i + 1] - 1)

for t, l in work:
    k = max(k, required_k[t])
    h = t - k
    if h < 0:
        print(-1)
        exit()
    ans += h

print(ans)