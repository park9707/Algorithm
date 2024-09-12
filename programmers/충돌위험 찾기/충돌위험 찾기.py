from collections import defaultdict


def solution(points, routes):
    visited = defaultdict(int)
    for route in routes:
        x, y = points[route[0]-1]
        visited[x, y, 0] += 1
        n = 1
        for i in route[1:]:
            r, c = points[i - 1]
            if r < x:
                for num in range(x-1, r-1, -1):
                    visited[num, y, n] += 1
                    n += 1
            elif r > x:
                for num in range(x+1, r+1):
                    visited[num, y, n] += 1
                    n += 1

            if c < y:
                for num in range(y-1, c-1, -1):
                    visited[r, num, n] += 1
                    n += 1
            elif c > y:
                for num in range(y+1, c+1):
                    visited[r, num, n] += 1
                    n += 1

            x, y = r, c

    return sum(1 if v > 1 else 0 for v in visited.values())
