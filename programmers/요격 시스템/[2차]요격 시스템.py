def solution(targets):
    answer = 0
    targets.sort(key=lambda x: (x[1], x[0]))
    a = 0
    for s, e in targets:
        if a <= s:
            a = e
            answer += 1

    return answer
