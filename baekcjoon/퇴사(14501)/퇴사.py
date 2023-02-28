n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [0] * (n + 1)
for d in range(n - 1, -1, -1):
    if d + arr[d][0] > n:
        result[d] = result[d + 1]
    else:
        result[d] = max(result[d + 1], result[d + arr[d][0]] + arr[d][1])

print(result[0])