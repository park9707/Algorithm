import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
ans = []
ref = float('inf')

for i in range(N - 2):
    p = arr[i]
    l = i + 1
    r = N - 1
    while l < r:
        v = arr[l] + arr[r] + p
        if abs(v) < ref:
            ref = abs(v)
            ans = [p, arr[l], arr[r]]
        if v < 0:
            l += 1
        elif v > 0:
            r -= 1
        else:
            print(*ans)
            exit()

print(*ans)