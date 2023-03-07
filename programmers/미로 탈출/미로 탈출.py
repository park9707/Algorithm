from collections import deque


def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                sx, sy = j, i
            elif maps[i][j] == 'L':
                lx, ly = j, i

    def bfs(x, y, g):
        visited = [[0] * len(maps[0]) for _ in range(len(maps))]
        q = deque([(x, y)])
        visited[y][x] = 1

        while q:
            x, y = q.popleft()
            if maps[y][x] == g:
                return visited[y][x] - 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps):
                    if maps[ny][nx] != 'X' and visited[ny][nx] == 0:
                        q.append((nx, ny))
                        visited[ny][nx] = visited[y][x] + 1
        return 0

    answer = bfs(sx, sy, 'L')
    if answer == 0:
        return -1

    tmp = answer
    answer += bfs(lx, ly, 'E')

    return answer if answer != tmp else -1