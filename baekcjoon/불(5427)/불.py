import sys, collections
input = sys.stdin.readline


def bfs():
    w, h = map(int, input().split())
    fire = collections.deque()
    sg = collections.deque()
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        temp = list(input().rstrip())
        for j in range(w):
            if temp[j] == '#':
                visited[i][j] = 2
            elif temp[j] == '*':
                fire.append([i, j])
                visited[i][j] = 2
            elif temp[j] == '@':
                sg.append([i, j])
                visited[i][j] = 1
    ans = 0
    while sg:
        ans += 1
        n = len(fire)
        for _ in range(n):
            x, y = fire.popleft()
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] < 2:
                    visited[nx][ny] = 2
                    fire.append([nx, ny])

        n = len(sg)
        for _ in range(n):
            x, y = sg.popleft()
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w:
                    if not visited[nx][ny]:
                        sg.append([nx, ny])
                        visited[nx][ny] = 1
                else:
                    return ans

    return 'IMPOSSIBLE'


t = int(input())
move = ((0, 1), (1, 0), (-1, 0), (0, -1))
for _ in range(t):
    print(bfs())