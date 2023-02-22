from sys import stdin
input = stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

for i in range(1, n):
    arr[i] = max(arr[i], arr[i-1] + arr[i])

print(max(arr))