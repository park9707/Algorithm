def solution(commands):
    answer = []
    merged = [[(i, j) for j in range(51)] for i in range(51)]
    board = [['EMPTY'] * 51 for _ in range(51)]

    for command in commands:
        command = command.split()
        if command[0] == 'UPDATE':
            if len(command) == 4:
                r, c, value = int(command[1]), int(command[2]), command[3]
                x, y = merged[r][c]
                board[x][y] = value
            else:
                value1, value2 = command[1], command[2]
                for i in range(1, 51):
                    for j in range(1, 51):
                        if board[i][j] == value1:
                            board[i][j] = value2

        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, command[1:])
            x1, y1 = merged[r1][c1]
            x2, y2 = merged[r2][c2]
            if board[x1][y1] == "EMPTY":
                board[x1][y1] = board[x2][y2]
            for i in range(1, 51):
                for j in range(1, 51):
                    if merged[i][j] == (x2, y2):
                        merged[i][j] = (x1, y1)

        elif command[0] == 'UNMERGE':
            r, c = map(int, command[1:])
            x, y = merged[r][c]
            tmp = board[x][y]
            for i in range(1, 51):
                for j in range(1, 51):
                    if merged[i][j] == (x, y):
                        merged[i][j] = (i, j)
                        board[i][j] = "EMPTY"
            board[r][c] = tmp

        elif command[0] == 'PRINT':
            r, c = map(int, command[1:])
            x, y = merged[r][c]
            answer.append(board[x][y])

    return answer
