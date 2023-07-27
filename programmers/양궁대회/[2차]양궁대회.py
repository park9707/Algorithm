from copy import deepcopy


def cal(ryan, apeech):
    global answer
    score = 0
    for i in range(11):
        if ryan[i] > apeech[i]:
            score += 10 - i
        elif apeech[i] > 0:
            score -= 10 - i
    if score > 0:
        answer.append([score, deepcopy(ryan)])


def shoot(cnt, i, ryan, apeech):
    if cnt == 0:
        cal(ryan, apeech)
        return

    for j in range(i, 10):
        temp = apeech[j] + 1
        if temp <= cnt:
            cnt -= temp
            ryan[j] = temp
            shoot(cnt, j+1, ryan, apeech)
            ryan[j] = 0
            cnt += temp
    ryan[10] = cnt
    cal(ryan, apeech)
    ryan[10] = 0


def solution(n, info):
    global answer
    answer = []
    shoot(n, 0, [0 for _ in range(11)], info)
    answer.sort(key=lambda x: [x[0], x[1][::-1]], reverse=True)
    return answer[0][1] if answer else [-1]
