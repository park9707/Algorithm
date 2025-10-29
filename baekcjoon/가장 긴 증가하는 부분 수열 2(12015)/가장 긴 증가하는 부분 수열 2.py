import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = [arr[0]]

for i in range(1, n):
    if s[-1] < arr[i]:
        s.append(arr[i])
    elif s[-1] == arr[i]:
        continue
    else:
        idx = bisect_left(s, arr[i])
        s[idx] = arr[i]

print(len(s))