import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
p = nums[0]
n = p
values = [1] * p

for i in nums[1:]:
    if i >= n:
        continue
    pre = n
    n = i
    for j in range(n, pre):
        values[j % n] += values[j]

v = 0
for i in range(1, n):
    v += values[i] * i

print(v / p)