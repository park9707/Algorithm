import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(str, input().rstrip().split())) for _ in range(n)]
tmp_num = int(board[0][0])
visited = [[[float('-inf'), float('inf')] for _ in range(n)] for _ in range(n)]
arr = {(1, 0), (0, 1)}
visited[1][0][0] = visited[0][1][0] = visited[1][0][1] = visited[0][1][1] = tmp_num
move = ((0, 1), (1, 0))

while arr:
    new_arr = set()
    for x, y in arr:
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if nx < n and ny < n:
                next_num = int(board[nx][ny])
                if board[x][y] == '+':
                    max_num = visited[x][y][0] + next_num
                    min_num = visited[x][y][1] + next_num
                elif board[x][y] == '-':
                    max_num = visited[x][y][0] - next_num
                    min_num = visited[x][y][1] - next_num
                else:
                    max_num = visited[x][y][0] * next_num
                    min_num = visited[x][y][1] * next_num

                visited[nx][ny][0] = max(visited[nx][ny][0], max_num)
                visited[nx][ny][1] = min(visited[nx][ny][1], min_num)

                for ndx, ndy in move:
                    nnx, nny = nx + ndx, ny + ndy
                    if nnx < n and nny < n:
                        visited[nnx][nny][0] = max(visited[nnx][nny][0], visited[nx][ny][0])
                        visited[nnx][nny][1] = min(visited[nnx][nny][1], visited[nx][ny][1])
                        new_arr.add((nnx, nny))

    arr = new_arr

print(visited[n-1][n-1][0], visited[n-1][n-1][1])