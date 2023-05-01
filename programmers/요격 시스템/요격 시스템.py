def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    m = -1

    for target in targets:
        if target[0] >= m:
            answer += 1
            m = target[1]
    return answer
