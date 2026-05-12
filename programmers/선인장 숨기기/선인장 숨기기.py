from collections import deque


def solution(m, n, h, w, drops):
    rain = [[float('inf')] * n for _ in range(m)]
    for i in range(1, len(drops) + 1):
        x, y = drops[i - 1]
        rain[x][y] = i

    row_min = [[float('inf')] * (n - w + 1) for _ in range(m)]

    for i in range(m):
        q = deque()

        for j in range(w - 1):
            while q and rain[i][q[-1]] >= rain[i][j]:
                q.pop()

            q.append(j)

        for j in range(w - 1, n):
            while q and rain[i][q[-1]] >= rain[i][j]:
                q.pop()

            q.append(j)

            if q[0] <= j - w:
                q.popleft()

            row_min[i][j - w + 1] = rain[i][q[0]]

    best = -1
    ans = [0, 0]

    final_min = [[float('inf')] * (n - w + 1) for _ in range(m - h + 1)]

    for y in range(n - w + 1):
        q = deque()

        for x in range(h - 1):
            while q and row_min[q[-1]][y] >= row_min[x][y]:
                q.pop()

            q.append(x)

        for x in range(h - 1, m):
            while q and row_min[q[-1]][y] >= row_min[x][y]:
                q.pop()

            q.append(x)

            if q[0] <= x - h:
                q.popleft()

            if x >= h - 1:
                start_row = x - h + 1
                final_min[start_row][y] = row_min[q[0]][y]

    for x in range(m - h + 1):
        for y in range(n - w + 1):
            if final_min[x][y] > best:
                best = final_min[x][y]
                ans = [x, y]

    return ans