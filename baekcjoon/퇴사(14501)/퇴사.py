n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = [0] * (n + 1)
for d in range(n - 1, -1, -1):
    if d + arr[d][0] > n:
        answer[d] = answer[d + 1]
    else:
        answer[d] = max(answer[d + 1], answer[d + arr[d][0]] + arr[d][1])

print(answer[0])