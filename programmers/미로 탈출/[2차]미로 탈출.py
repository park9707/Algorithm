from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    move = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for i in range(n):
        for j in range(m):
            tmp = maps[i][j]
            if tmp == 'S':
                start = [i, j]
            elif tmp == 'L':
                lever = [i, j]
            elif tmp == 'E':
                end = [i, j]

    def bfs(s, e):
        q = deque([[s[0], s[1], 0]])
        visited = [[False] * m for _ in range(n)]
        visited[s[0]][s[1]] = True
        ex, ey = e
        while q:
            x, y, cnt = q.popleft()
            for dx, dy in move:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X':
                    if not visited[nx][ny]:
                        if nx == ex and ny == ey:
                            return cnt + 1
                        else:
                            visited[nx][ny] = True
                            q.append([nx, ny, cnt + 1])
        return -1

    first = bfs(start, lever)
    if first == -1:
        return -1
    second = bfs(lever, end)
    return first + second if second != -1 else -1
