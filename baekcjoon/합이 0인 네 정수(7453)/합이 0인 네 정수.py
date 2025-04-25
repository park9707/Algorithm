import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ab, cd = [], []
ans = 0
for i in range(n):
    for j in range(n):
        ab.append(arr[i][0] + arr[j][1])
        cd.append(arr[i][2] + arr[j][3])

ab.sort()
cd.sort()
n *= n
l, r = 0, n - 1
num = ab[0]

while l < r:
    mid = (l + r) // 2
    if num + cd[mid] < 0:
        l = mid + 1
    elif num + cd[mid] > 0:
        r = mid - 1
    else:
        while mid + 1 < n and cd[mid + 1] == cd[mid]:
            mid += 1
        r = mid
        break

a, c = 0, r
while a < n and c >= 0:
    if ab[a] + cd[c] < 0:
        a += 1
    elif ab[a] + cd[c] > 0:
        c -= 1
    else:
        next_a, next_c = a, c
        while next_a + 1 < n and ab[next_a] == ab[next_a + 1]:
            next_a += 1
        while next_c - 1 >= 0 and cd[next_c] == cd[next_c - 1]:
            next_c -= 1
        ans += ((next_a - a + 1) * (c - next_c + 1))
        a = next_a + 1
        c = next_c - 1

print(ans)