from collections import deque

def solution(board):
    n = len(board) - 1
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = [[[0] * 2 for _ in range(n + 1)] for _ in range(n + 1)]
    q = deque()
    q.append([0, 0, 0, 1, 0, 0])
    while q:
        x1, y1, x2, y2, cnt, state = q.popleft()
        visited[x1][y1][state] = visited[x2][y2][state] = 1

        for i in range(4):
            dx = move[i][0]
            dy = move[i][1]
            nx1 = x1 + dx
            ny1 = y1 + dy
            nx2 = x2 + dx
            ny2 = y2 + dy

            if 0 <= nx1 <= n and 0 <= nx2 <= n and 0 <= ny1 <= n and 0 <= ny2 <= n:
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                    if visited[nx1][ny1][state] == 0 or visited[nx2][ny2][state] == 0:
                        if (nx1 == n and ny1 == n) or (nx2 == n and ny2 == n):
                            return cnt + 1
                        q.append([nx1, ny1, nx2, ny2, cnt + 1, state])
                        visited[nx1][ny1][state] = visited[nx2][ny2][state] = 1

        if state == 1:
            for dx, dy in move[2:]:
                ny1 = y1 + dy
                if 0 <= ny1 <= n:
                    if board[x1][ny1] == 0 and board[x2][ny1] == 0:
                        if visited[x1][ny1][0] == 0 or visited[x1][y1][0] == 0:
                            if x1 == n and ny1 == n:
                                return cnt + 1
                            q.append([x1, y1, x1, ny1, cnt + 1, 0])
                            visited[x1][y1][0] = visited[x1][ny1][0] = 1

                ny2 = y2 + dy
                if 0 <= ny2 <= n:
                    if board[x2][ny2] == 0 and board[x1][ny2] == 0:
                        if visited[x2][ny2][0] == 0 or visited[x2][y2][0] == 0:
                            if x2 == n and ny2 == n:
                                return cnt + 1
                            q.append([x2, y2, x2, ny2, cnt + 1, 0])
                            visited[x2][y2][0] = visited[x2][ny2][0] = 1

        else:
            for dx, dy in move[:2]:
                nx1 = x1 + dx
                if 0 <= nx1 <= n:
                    if board[nx1][y1] == 0 and board[nx1][y2] == 0:
                        if visited[nx1][y1][1] == 0 or visited[x1][y1][1] == 0:
                            if nx1 == n and y1 == n:
                                return cnt + 1
                            q.append([x1, y1, nx1, y1, cnt + 1, 1])
                            visited[x1][y1][1] = visited[nx1][y1][1] = 1

                nx2 = x2 + dx
                if 0 <= nx2 <= n:
                    if board[nx2][y1] == 0 and board[nx2][y2] == 0:
                        if visited[nx2][y2][1] == 0 or visited[x2][y2][1] == 0:
                            if nx2 == n and y2 == n:
                                return cnt + 1
                            q.append([x2, y2, nx2, y2, cnt + 1, 1])
                            visited[x2][y2][1] = visited[nx2][y2][1] = 1
