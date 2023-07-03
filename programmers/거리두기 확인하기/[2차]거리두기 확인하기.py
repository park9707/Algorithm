def solution(places):
    answer = []
    move = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(x, y, depth):
        result = 1
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                if tmp[nx][ny] != 'X' and depth < 2:
                    if tmp[nx][ny] == 'O':
                        visited[nx][ny] = True
                        result = min(result, dfs(nx, ny, depth + 1))
                        visited[nx][ny] = False
                    elif tmp[nx][ny] == 'P':
                        return 0
        return result

    visited = [[False] * 5 for _ in range(5)]
    for place in places:
        tmp = [list(i) for i in place]
        a = 1
        for i in range(5):
            for j in range(5):
                if tmp[i][j] == 'P':
                    visited[i][j] = True
                    result = dfs(i, j, 0)
                    visited[i][j] = False
                    if not result:
                        answer.append(0)
                        a = 0
                        break
            if a == 0:
                break
        else:
            answer.append(1)

    return answer