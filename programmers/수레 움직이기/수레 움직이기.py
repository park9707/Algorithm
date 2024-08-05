from collections import deque


def solution(maze):
    answer = int(1e9)
    red_start_x, red_start_y, blue_start_x, blue_start_y, red_end_x, red_end_y, blue_end_x, blue_end_y = 0, 0, 0, 0, 0, 0, 0, 0
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 1:
                red_start_x, red_start_y = x, y
            if maze[x][y] == 2:
                blue_start_x, blue_start_y = x, y
            if maze[x][y] == 3:
                red_end_x, red_end_y = x, y
            if maze[x][y] == 4:
                blue_end_x, blue_end_y = x, y
    q = deque()
    red_visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    blue_visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    red_visited[red_start_x][red_start_y] = True
    blue_visited[blue_start_x][blue_start_y] = True

    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    q.append((red_start_x, red_start_y, blue_start_x, blue_start_y, red_visited, blue_visited, 0))
    while q:
        red_x, red_y, blue_x, blue_y, red_visited, blue_visited, cnt = q.popleft()
        if (red_x, red_y) == (red_end_x, red_end_y) and (blue_x, blue_y) == (blue_end_x, blue_end_y):
            answer = min(answer, cnt)
            continue

        # 빨강만 먼저 도착한 경우
        if (red_x, red_y) == (red_end_x, red_end_y):
            for blue_idx in range(4):
                _blue_x, _blue_y = blue_x + dx[blue_idx], blue_y + dy[blue_idx]

                # 범위 안에 있기, 벽X, 방문X, 파랑빨강 같은 곳에 위치X
                if -1 < _blue_x < len(maze) and -1 < _blue_y < len(maze[0]) and maze[_blue_x][_blue_y] != 5 and \
                        blue_visited[_blue_x][_blue_y] == False \
                        and not ((red_x == _blue_x and red_y == _blue_y)):
                    # 방문경로를 다시 설정
                    new_red_visited = [rv[:] for rv in red_visited]
                    new_blue_visited = [bv[:] for bv in blue_visited]
                    new_blue_visited[_blue_x][_blue_y] = True
                    q.append((red_x, red_y, _blue_x, _blue_y, new_red_visited, new_blue_visited, cnt + 1))

        # 파랑만 먼저 도착한 경우
        elif (blue_x, blue_y) == (blue_end_x, blue_end_y):
            for red_idx in range(4):
                _red_x, _red_y = red_x + dx[red_idx], red_y + dy[red_idx]
                if -1 < _red_x < len(maze) and -1 < _red_y < len(maze[0]) and maze[_red_x][_red_y] != 5 and \
                        red_visited[_red_x][_red_y] == False \
                        and not ((_red_x == blue_x and _red_y == blue_y)):
                    new_red_visited = [rv[:] for rv in red_visited]
                    new_blue_visited = [bv[:] for bv in blue_visited]
                    new_red_visited[_red_x][_red_y] = True
                    q.append((_red_x, _red_y, blue_x, blue_y, new_red_visited, new_blue_visited, cnt + 1))

        # 둘다 도착하지 못한 경우
        else:
            for red_idx in range(4):
                _red_x, _red_y = red_x + dx[red_idx], red_y + dy[red_idx]
                if -1 < _red_x < len(maze) and -1 < _red_y < len(maze[0]) and maze[_red_x][_red_y] != 5 and \
                        red_visited[_red_x][_red_y] == False:
                    for blue_idx in range(4):
                        _blue_x, _blue_y = blue_x + dx[blue_idx], blue_y + dy[blue_idx]
                        if -1 < _blue_x < len(maze) and -1 < _blue_y < len(maze[0]) and maze[_blue_x][_blue_y] != 5 and \
                                blue_visited[_blue_x][_blue_y] == False \
                                and not ((_red_x == _blue_x) and (_red_y == _blue_y)):
                            # 이동하려는 red좌표가 현재의 blue좌표이고, 이동하려는 blue좌표가 현재의 red좌표인 경우 X
                            if (_red_x == blue_x) and (_red_y == blue_y) and (_blue_x == red_x) and (
                                    _blue_y == red_y): continue
                            new_red_visited = [rv[:] for rv in red_visited]
                            new_blue_visited = [bv[:] for bv in blue_visited]
                            new_red_visited[_red_x][_red_y] = True
                            new_blue_visited[_blue_x][_blue_y] = True
                            q.append((_red_x, _red_y, _blue_x, _blue_y, new_red_visited, new_blue_visited, cnt + 1))
    if answer == int(1e9):
        return 0
    return answer