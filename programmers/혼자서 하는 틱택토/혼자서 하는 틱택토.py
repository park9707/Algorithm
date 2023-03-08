from collections import Counter


def solution(board):
    cnt = Counter([i for b in board for i in b])
    if cnt['O'] != cnt['X'] and cnt['O'] != cnt['X'] + 1:
        return 0

    victory = [[[0, 0], [0, 1], [0, 2]]
        , [[1, 0], [1, 1], [1, 2]]
        , [[2, 0], [2, 1], [2, 2]]
        , [[0, 0], [1, 0], [2, 0]]
        , [[0, 1], [1, 1], [2, 1]]
        , [[0, 2], [1, 2], [2, 2]]
        , [[0, 0], [1, 1], [2, 2]]
        , [[0, 2], [1, 1], [2, 0]]]

    def check_vic(a):
        for vic in victory:
            for y, x in vic:
                if board[y][x] != a:
                    break
            else:
                return 1
        return 0

    o_v = check_vic('O')
    x_v = check_vic('X')

    if o_v + x_v == 2:
        return 0

    if o_v == 1 and cnt['O'] + 1 == cnt['X']:
        return 1

    if x_v == 1 and cnt['O'] == cnt['X']:
        return 1

    if (cnt['O'] == cnt['X'] and o_v != 1) or (cnt['O'] == cnt['X'] + 1 and x_v != 1):
        return 1

    return 0
