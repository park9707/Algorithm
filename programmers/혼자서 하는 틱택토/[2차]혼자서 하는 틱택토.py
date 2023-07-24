from collections import Counter


def solution(board):
    # O와 X의 수로만 나올 수도 있는 경기인지 판단
    cnt = Counter([i for b in board for i in b])
    if cnt['X'] != cnt['O'] and cnt['X'] + 1 != cnt['O']:
        return 0

    # 이기는 경우의 수
    victory = [[[0, 0], [0, 1], [0, 2]],
               [[1, 0], [1, 1], [1, 2]],
               [[2, 0], [2, 1], [2, 2]],
               [[0, 0], [1, 0], [2, 0]],
               [[0, 1], [1, 1], [2, 1]],
               [[0, 2], [1, 2], [2, 2]],
               [[0, 0], [1, 1], [2, 2]],
               [[0, 2], [1, 1], [2, 0]]]

    result = 0
    # 결과 값 차이 두기 위해 인덱스 1번부터
    for i, c in enumerate(['O', 'X'], 1):
        # 승리 조건 하나씩 받아서 체크
        for v in victory:
            for x, y in v:
                # 승리가 아니라면 break
                if board[x][y] != c:
                    break
            # 승리를 했다면 O가 승리시 1, X가 승리시 2를 더함
            else:
                result += i
                break

    # O가 승리했다면 O의 수가 하나 더 많아야 하고, X가 승리했다면 O와 X의 수가 같아야 한다.
    if (result == 1 and cnt['O'] == cnt['X']) or (result == 2 and cnt['O'] > cnt['X']):
        return 0
    # 둘 다 승리했다면 나올 수 없는 판
    if result == 3:
        return 0
    return 1
