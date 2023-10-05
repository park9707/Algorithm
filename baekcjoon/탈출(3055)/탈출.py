import sys
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())

board = [list(input().rstrip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
water = []
stack = []
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
end_x = end_y = 0

for i in range(r):
    for j in range(c):
        if board[i][j] == '.':
            continue
        elif board[i][j] == 'D':
            end_x, end_y = i, j
            continue
        elif board[i][j] == 'S':
            stack.append([i, j])
        elif board[i][j] == '*':
            water.append([i, j])
        visited[i][j] = 1

t = 0
while stack:
    t += 1
    temp = []
    for x, y in water:
        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < r and 0 <= ny < c and not (nx == end_x and ny == end_y):
                if visited[nx][ny] != 1:
                    temp.append([nx, ny])
                    visited[nx][ny] = 1
    water = temp
    temp = []

    for x, y in stack:
        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < r and 0 <= ny < c:
                if nx == end_x and ny == end_y:
                    print(t)
                    exit(0)
                elif not visited[nx][ny]:
                    temp.append([nx, ny])
                    visited[nx][ny] = 2
    stack = temp

print('KAKTUS')
