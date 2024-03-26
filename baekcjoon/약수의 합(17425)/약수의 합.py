import sys
input = sys.stdin.readline

MAX = 1000000
arr = [i + 1 for i in range(MAX + 1)]
arr[1] = 1
s = 1
for i in range(2, MAX // 2 + 1):
    for j in range(i + i, MAX + 1, i):
        arr[j] += i

for i in range(2, MAX + 1):
    s += arr[i]
    arr[i] = s

for i in range(int(input())):
    sys.stdout.write(str(arr[int(input())]) + '\n')
