import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0

for p in range(n - 2):
    l, r = p + 1, n - 1
    while l < r:
        num = arr[p] + arr[l] + arr[r]
        if num > 0:
            r -= 1
        else:
            if num == 0:
                if arr[l] == arr[r]:
                    ans += r - l
                else:
                    idx = bisect_left(arr, arr[r])
                    ans += r - idx + 1
            l += 1

print(ans)