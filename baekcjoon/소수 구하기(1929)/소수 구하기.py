import math
import sys

m, n = map(int,sys.stdin.readline().split())

arr = [True] * (n+1)
arr[1] = False

for i in range(2, int(math.sqrt(n))+1):
    if arr[i] == True:
        for j in range(i+i, n+1, i):
            arr[j] = False

[sys.stdout.write(str(i)+'\n') for i in range(m, n+1) if arr[i] == True]
