import sys
input = sys.stdin.readline


def dfs(node):
    if not tree[node]:
        return 1

    cnt = 0
    for next_node in tree[node]:
        cnt += dfs(next_node)

    return cnt


n = int(input())
parents = list(map(int, input().split()))
d = int(input())
tree = [[] for _ in range(n)]
start = 0

for i in range(len(parents)):
    if parents[i] == -1:
        start = i
        continue
    tree[parents[i]].append(i)

tree[d] = []
ans = dfs(start) - 1
if len(tree[parents[d]]) == 1:
    ans += 1

print(ans)