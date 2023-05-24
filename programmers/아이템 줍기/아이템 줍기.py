from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    maps = [[0] * 104 for _ in range(104)]
    visited = [[-1] * 104 for _ in range(104)]
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i in range(len(rectangle)):
        for j in range(len(rectangle[0])):
            rectangle[i][j] *= 2

    for left_x, left_y, right_x, right_y in rectangle:
        for y in range(left_y + 1, right_y):
            for x in range(left_x + 1, right_x):
                maps[y][x] = 2

        for i in range(left_y, right_y + 1):
            if maps[i][left_x] == 0:
                maps[i][left_x] = 1
            if maps[i][right_x] == 0:
                maps[i][right_x] = 1

        for j in range(left_x, right_x + 1):
            if maps[left_y][j] == 0:
                maps[left_y][j] = 1
            if maps[right_y][j] == 0:
                maps[right_y][j] = 1

    q = deque()
    q.append([characterX, characterY])
    visited[characterY][characterX] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            dx, dy = move[i]
            nx = dx + x
            ny = dy + y

            if maps[ny][nx] == 1 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                if nx == itemX and ny == itemY:
                    return visited[ny][nx] // 2
                q.append([nx, ny])
