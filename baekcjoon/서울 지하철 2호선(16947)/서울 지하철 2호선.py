import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find_cycle(station, now):
    global check
    global target
    for nx in wire[now]:
        if nx != station[-2]:
            if visited[nx] == -1:
                visited[now] = -2
                find_cycle(station + [nx], nx)
                if check:
                    if target != 0:
                        visited[now] = 0
                        if target == now:
                            target = 0
                    return

            else:
                check = True
                target = nx
                visited[now] = 0
                return


def dfs(cnt, now):
    visited[now] = cnt
    for nx in wire[now]:
        if visited[nx] < 0:
            dfs(cnt + 1, nx)


n = int(input())
wire = [[] for _ in range(n + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    wire[a].append(b)
    wire[b].append(a)

visited = [-1] * (n + 1)
check = False
target = n + 1
find_cycle([0, 1], 1)

for i in range(1, n + 1):
    if len(wire[i]) > 2 and visited[i] == 0:
        for nx in wire[i]:
            if visited[nx] != 0:
                dfs(1, nx)

print(*visited[1:])