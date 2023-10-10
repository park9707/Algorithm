import sys

globalPaperCnt = float("inf")


def solution():
    read = sys.stdin.readline
    board = [list(map(int, read().split())) for _ in range(10)]
    papers = [0, 0, 0, 0, 0, 0]

    # 색종이를 붙일 수 있는지 확인
    def isPossibleToAttach(y, x, s):
        for i in range(s):
            for j in range(s):
                if not board[y + i][x + j]: return False
        return True

    def attachOrDetachPaper(y, x, s, b):
        for i in range(s):
            for j in range(s):
                board[y + i][x + j] = b

    def dfsProc(y, x, currPaperCnt):
        global globalPaperCnt
        # x, y가 0이라면 반복
        while not board[y][x]:
            x += 1
            if x >= 10:
                y += 1
                if y >= 10:
                    globalPaperCnt = min(globalPaperCnt, currPaperCnt)
                    return
                x = 0

        # 최소 종이 수를 넘었다면 더 확인하지 않음
        if globalPaperCnt <= currPaperCnt: return


        for s in range(1, 6):
            # 종이를 다썼다면 continue
            if papers[s] == 5:
                continue
            # 색종이가 종이를 넘어 간다면 더 큰 색종이는 볼 필요 없으므로 break
            if x + s > 10 or y + s > 10:
                break

            if isPossibleToAttach(y, x, s):
                attachOrDetachPaper(y, x, s, 0)
                papers[s] += 1
                dfsProc(y, s, currPaperCnt + 1)
                attachOrDetachPaper(y, x, s, 1)
                papers[s] -= 1

    dfsProc(0, 0, 0)
    global globalPaperCnt
    if globalPaperCnt == float("inf"): globalPaperCnt = -1
    print(globalPaperCnt)


solution()