import sys

n = int(input())

arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

for i,j in sorted(arr):
    sys.stdout.write(str(i)+' '+str(j)+'\n')
