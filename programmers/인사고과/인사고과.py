def solution(scores):
    answer = 1
    w = scores[0]
    w_score = sum(w)
    colleague_s = 0
    for score in sorted(scores, key=lambda x: (-x[0], x[1])):
        if score[0] > w[0] and score[1] > w[1]:
            return -1
        if colleague_s <= score[1]:
            if w_score < sum(score):
                answer += 1
            colleague_s = score[1]

    return answer
