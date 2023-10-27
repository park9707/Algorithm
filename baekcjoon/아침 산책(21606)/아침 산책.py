import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(num, cnt):
    for l in line[num]:
        if is_inside[l]:
            cnt += 1
        elif not visited[l]:
            visited[l] = True
            cnt = dfs(l, cnt)
    return cnt


n = int(input())
a = input().rstrip()
ans = 0

is_inside = [True] * (n + 1)

for i in range(n):
    if int(a[i]) == 0:
        is_inside[i + 1] = False

line = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    i, j = map(int, input().split())
    if is_inside[i] and is_inside[j]:
        ans += 2
    line[i].append(j)
    line[j].append(i)

visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not is_inside[i] and not visited[i]:
        visited[i] = True
        temp = dfs(i, 0)
        ans += temp * (temp - 1)

print(ans)