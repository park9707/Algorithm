import sys
from copy import deepcopy
input = sys.stdin.readline


def move_fish(new_board, new_location, new_d):
    for fish_num in range(1, 17):
        x, y = new_location[fish_num]
        if new_board[x][y] != fish_num:
            continue
        for i in range(8):
            direction = (new_d[fish_num] + i) % 8
            dx, dy = move[direction]
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                if new_board[nx][ny] < 17:
                    new_board[nx][ny], new_board[x][y] = new_board[x][y], new_board[nx][ny]
                    new_location[fish_num] = [nx, ny]
                    new_location[new_board[x][y]] = [x, y]
                    new_d[fish_num] = direction
                    break

    return new_board, new_location, new_d


def move_shark(new_board, new_location, new_d, x, y, cnt):
    global ans
    ans = max(ans, cnt)
    new_board[x][y] = 17
    dx, dy = move[new_d[17]]
    new_board, new_location, new_d = move_fish(new_board, new_location, new_d)
    new_board[x][y] = 0
    nx = x + dx
    ny = y + dy

    while 0 <= nx < 4 and 0 <= ny < 4:
        fish = new_board[nx][ny]
        if fish:
            new_d[17], new_d[fish] = new_d[fish], new_d[17]
            move_shark(deepcopy(new_board), deepcopy(new_location), deepcopy(new_d), nx, ny, cnt + fish)
            new_d[17], new_d[fish] = new_d[fish], new_d[17]
        nx += dx
        ny += dy


ans = 0
move = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
board = [[] for _ in range(4)]
location = [[] for _ in range(17)]
d = [[] for _ in range(18)]
for i in range(4):
    temp = list(map(int, input().split()))
    for idx in range(0, 8, 2):
        num = temp[idx]
        d[num] = temp[idx + 1] - 1
        board[i].append(temp[idx])
        location[num] = [i, idx // 2]
d[17] = d[board[0][0]]
move_shark(board, location, d, 0, 0, board[0][0])

print(ans)
