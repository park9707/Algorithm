def solution(n, m, section):
    answer = 0
    s = {0:0}
    for i in range(1, n+1):
        s[i] = 1
    for i in section:
        if s[i] == 0:
            continue
        for j in range(i, i+m):
            s[j] = 0
        answer += 1
    return answer
