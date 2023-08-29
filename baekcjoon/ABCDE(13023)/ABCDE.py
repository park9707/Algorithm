import sys, collections
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
relationship = collections.defaultdict(list)

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    relationship[a].append(b)
    relationship[b].append(a)
visited = [False] * n


def dfs(num, cnt):
    if cnt == 5:
        return True

    for j in relationship[num]:
        if not visited[j]:
            visited[j] = True
            if dfs(j, cnt + 1):
                return True
            visited[j] = False
    return False


for i in range(n):
    visited[i] = True
    if dfs(i, 1):
        print(1)
        break
    visited[i] = False
else:
    print(0)
