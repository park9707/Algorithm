import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

left_max = arr[0]
ans = 'YES'
for i in range(1, n):
    if arr[i] + k < left_max:
        ans = 'NO'
        break
    left_max = max(left_max, arr[i])

print(ans)