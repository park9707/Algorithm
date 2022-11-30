import sys

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

for i in sorted(arr):
    sys.stdout.write(str(i)+'\n')
