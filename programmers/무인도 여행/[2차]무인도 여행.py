import sys
sys.setrecursionlimit(10 ** 6)


def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    graph = [list(maps[i]) for i in range(n)]
    visited = [[False] * m for _ in range(n)]
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def dfs(x, y):
        global cnt
        visited[y][x] = True
        cnt += int(graph[y][x])

        for dx, dy in move:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and graph[ny][nx] != 'X':
                    dfs(nx, ny)

    global cnt

    for y in range(n):
        for x in range(m):
            if graph[y][x] != 'X':
                if not visited[y][x]:
                    cnt = 0
                    dfs(x, y)
                    answer.append(cnt)

    return sorted(answer) if len(answer) > 0 else [-1]
