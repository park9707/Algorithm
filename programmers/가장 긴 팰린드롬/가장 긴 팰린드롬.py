def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(len(s), i, -1):
            tmp = s[i:j]
            if tmp == tmp[::-1]:
                answer = max(answer, len(tmp))

    return answer
