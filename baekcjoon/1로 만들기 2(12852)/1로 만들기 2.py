import sys
input = sys.stdin.readline

n = int(input())
arr = [[float('inf'), 0] for _ in range(n + 1)]
arr[n][0] = 0

for i in range(n, 0, -1):
    if i % 3 == 0:
        arr[i//3][0] = arr[i][0] + 1
        arr[i//3][1] = i
    if i % 2 == 0:
        if arr[i//2][0] > arr[i][0] + 1:
            arr[i//2][0] = arr[i][0] + 1
            arr[i//2][1] = i
    if arr[i-1][0] > arr[i][0] + 1:
        arr[i-1][0] = arr[i][0] + 1
        arr[i-1][1] = i

ans = [1]
num = 1
while num != n:
    num = arr[num][1]
    ans.append(num)

print(len(ans) - 1)
print(*ans[::-1])