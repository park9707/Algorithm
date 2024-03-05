import sys, collections
input = sys.stdin.readline

N = int(input())
d = []
for _ in range(N):
    start_m, start_d, end_m, end_d = map(int, input().split())
    d.append([start_m * 100 + start_d, end_m * 100 + end_d])
q = collections.deque(sorted(d))
cnt = 0
start = 301
end = 0

while q:
    if start > 1130 or start < q[0][0]:
        break

    while q:
        s, e = q.popleft()
        if start >= s:
            if end <= e:
                end = e
        else:
            q.appendleft([s, e])
            break

    start = end
    cnt += 1

if start <= 1130:
    print(0)
else:
    print(cnt)