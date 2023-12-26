from collections import deque


def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil_amount = [0] * m
    move = ((0, 1), (1, 0), (-1, 0), (0, -1))

    for j in range(m):
        for i in range(n):
            if land[i][j] and not visited[i][j]:
                q = deque([[i, j]])
                cnt = 0
                r = j
                visited[i][j] = True
                while q:
                    cnt += 1
                    x, y = q.popleft()

                    for dx, dy in move:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] and not visited[nx][ny]:
                            q.append([nx, ny])
                            visited[nx][ny] = True
                            r = max(r, ny)

                for k in range(j, r + 1):
                    oil_amount[k] += cnt

    return max(oil_amount)