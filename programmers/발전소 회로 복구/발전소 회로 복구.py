from collections import deque


def solution(h, grid, panels, seqs):
    answer = 0
    grid = [list(row) for row in grid]
    panels = [[0]] + panels

    length = len(panels)
    n, m = len(grid), len(grid[0])
    dist = [[float('inf')] * length for _ in range(length)]
    move = ((0, 1), (1, 0), (0, -1), (-1, 0))

    for i in range(1, length - 1):
        _, x, y = panels[i]
        grid[x - 1][y - 1] = str(i)

    for i in range(1, length):
        q = deque([[panels[i][1] - 1, panels[i][2] - 1]])
        visited = [[-1] * m for _ in range(n)]
        visited[panels[i][1] - 1][panels[i][2] - 1] = 0
        dist[i][i] = 0
        while q:
            x, y = q.popleft()

            for dx, dy in move:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == -1 and grid[nx][ny] != '#':
                        q.append([nx, ny])
                        visited[nx][ny] = visited[x][y] + 1

                        if grid[nx][ny] == '@':
                            dist[i][0] = visited[nx][ny]
                        elif grid[nx][ny] != '.':
                            num = int(grid[nx][ny])
                            dist[i][num] = visited[nx][ny]

    for i in range(1, length):
        a = panels[i][0]
        for j in range(i + 1, length):
            b = panels[j][0]
            if a != b:
                dist[i][j] = dist[j][i] = dist[i][0] + abs(a - b) + dist[j][0]

    print(dist)

solution(3, [".#.##..", ".#..##.", ".......", "##.###.", ".@.#...", "...#..."], [[2, 3, 4], [2, 5, 6], [1, 1, 1], [3, 6, 3]], [[3, 2], [1, 2], [4, 1], [4, 3]])