import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
land = dict()
land_arr = []

# 섬 구분
land_num = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            q = deque([(i, j)])
            visited[i][j] = True
            land[(i, j)] = land_num
            land_arr.append((i, j, land_num))
            while q:
                x, y = q.popleft()
                for dx, dy in move:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        land[nx, ny] = land_num
                        land_arr.append((nx, ny, land_num))
            land_num += 1

# 다리 제작
edges = []
for x, y, cur_land in land_arr:
    for dx, dy in move:
        dist = 0
        nx = x + dx
        ny = y + dy
        while True:
            if 0 <= nx < n and 0 <= ny < m:
                to_land = land.get((nx, ny))
                # 섬이 있으면
                if to_land is not None:
                    # 같은 섬이라면 break
                    if cur_land == to_land:
                        break
                    # 다른 섬이지만 거리가 1이면 break
                    elif dist < 2:
                        break
                else:
                    nx += dx
                    ny += dy
                    dist += 1
                    continue
                edges.append((dist, cur_land, to_land))
                break
            else:
                break

edges.sort(reverse=True)


# 크루스칼
def find(k):
    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]


def union(a, b):
    a = find(a)
    b = find(b)
    parents[b] = a


ans = 0
cnt = land_num - 1
parents = [i for i in range(land_num)]
while cnt:
    if edges:
        w, x, y = edges.pop()
        if find(x) != find(y):
            union(x, y)
            ans += w
            cnt -= 1
    else:
        ans = -1
        break

print(ans)
