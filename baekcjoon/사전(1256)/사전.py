import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [[1] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

if arr[n][m] < k:
    print(-1)
    exit(0)

ans = ''
while 0 < n and 0 < m:
    if k <= arr[n-1][m]:
        ans += 'a'
        n -= 1
    else:
        ans += 'z'
        k -= arr[n-1][m]
        m -= 1

ans += 'z' * m + 'a' * n
print(ans)
