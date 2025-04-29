import sys, math
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = [0] * n
ans = 0

for i in range(n - 1):
    ratio = math.ceil(math.log2(a[i] / a[i + 1])) + b[i]
    if ratio > 0:
        b[i + 1] = ratio
        ans += ratio

print(ans)