from collections import deque


def solution(h, grid, panels, seqs):
    panels = [[0]] + panels

    length = len(panels)
    n, m = len(grid), len(grid[0])
    INF = float('inf')

    dist = [[INF] * length for _ in range(length)]
    move = ((0, 1), (1, 0), (0, -1), (-1, 0))

    er = ec = -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                er, ec = i, j

    for i in range(1, length):
        q = deque([[panels[i][1] - 1, panels[i][2] - 1]])
        visited = [[-1] * m for _ in range(n)]
        visited[panels[i][1] - 1][panels[i][2] - 1] = 0

        while q:
            x, y = q.popleft()

            for dx, dy in move:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == -1 and grid[nx][ny] != '#':
                        q.append([nx, ny])
                        visited[nx][ny] = visited[x][y] + 1

        dist[i][0] = visited[er][ec]
        dist[i][i] = 0

        for j in range(1, length):
            _, r, c = panels[j]
            dist[i][j] = visited[r - 1][c - 1]

    for i in range(1, length):
        a = panels[i][0]

        for j in range(1, length):
            b = panels[j][0]

            if a != b:
                dist[i][j] = dist[i][0] + abs(a - b) + dist[j][0]

    need = [0] * length

    for a, b in seqs:
        need[b] |= 1 << (a - 1)

    dp = [[INF] * length for _ in range(2 ** (length - 1))]
    dp[0][1] = 0

    for mask in range(2 ** (length - 1)):
        for cur in range(1, length):
            if dp[mask][cur] == INF:
                continue

            for nxt in range(1, length):
                bit = 1 << (nxt - 1)

                if mask & bit:
                    continue

                if (mask & need[nxt]) != need[nxt]:
                    continue

                next_mask = mask | bit

                dp[next_mask][nxt] = min(
                    dp[next_mask][nxt],
                    dp[mask][cur] + dist[cur][nxt]
                )

    full = (1 << (length - 1)) - 1
    return min(dp[full][i] for i in range(1, length))