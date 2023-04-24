def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    arr = [[0] * (m+1) for _ in range(n+1)]

    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree = -degree
        arr[r1][c1] += degree
        arr[r2+1][c2+1] += degree
        arr[r1][c2+1] += -degree
        arr[r2+1][c1] += -degree

    for i in range(n):
        for j in range(1, m):
            arr[i][j] += arr[i][j-1]

    for i in range(1, n+1):
        for j in range(m):
            arr[i][j] += arr[i-1][j]
            board[i-1][j] += arr[i-1][j]
            if board[i-1][j] > 0:
                answer += 1

    return answer
