from itertools import combinations


def solution(dice):
    def sum_score(arr, depth, score, score_arr):
        if depth == n // 2:
            score_arr.append(score)
            return

        d = dice[arr[depth-1] - 1]

        for s in d:
            sum_score(arr, depth + 1, score + s, score_arr)

    answer = []
    n = len(dice)
    arr = list(map(list, combinations(range(1, n + 1), n // 2)))
    max_cnt = 0

    for dice_a in arr:
        choice = [False] * (n + 1)
        for i in dice_a:
            choice[i] = True

        dice_b = []

        for i in range(1, n + 1):
            if not choice[i]:
                dice_b.append(i)

        score_a = []
        score_b = []
        sum_score(dice_a, 0, 0, score_a)
        sum_score(dice_b, 0, 0, score_b)
        score_a.sort()
        score_b.sort()
        win_cnt = 0
        for num in score_a:
            r = len(score_b)
            l = 0
            while l < r:
                mid = (l + r) // 2
                if num <= score_b[mid]:
                    r = mid
                else:
                    l = mid + 1

            win_cnt += l

        if max_cnt < win_cnt:
            max_cnt = win_cnt
            answer = dice_a

    return answer
