import sys
input = sys.stdin.readline


def move(arr):
    cnt, dist = K, 0
    while arr:
        d, num = arr.pop()
        if cnt == K:
            dist += (S - d) * 2

        if cnt < num:
            num -= cnt
            arr.append([d, num])
        elif cnt > num:
            cnt -= num
            continue

        cnt = K

    return dist


N, K, S = map(int, input().split())
l, r = [], []

for _ in range(N):
    a, b = map(int, input().split())
    if a < S:
        l.append([a, b])
    else:
        r.append([a, b])

l.sort(reverse=True)
r.sort()

print(move(l) + -move(r))