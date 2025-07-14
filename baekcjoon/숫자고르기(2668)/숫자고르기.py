import sys
input = sys.stdin.readline


def dfs(num, idx):
    visited[num] = True
    num = arr[num]
    if not visited[num]:
        dfs(num, idx)
    elif idx == num:
        ans.append(num)


n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
ans = []

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i)

print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])