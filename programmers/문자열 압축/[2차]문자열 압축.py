def solution(s):
    n = len(s)
    answer = n

    for i in range(1, n // 2 + 1):
        cnt = 1
        tmp = s[:i]
        a = ''
        for j in range(i, n, i):
            if s[j:j + i] == tmp:
                cnt += 1
            else:
                if cnt != 1:
                    a += str(cnt)
                a += tmp
                tmp = s[j:j + i]
                cnt = 1

        if cnt != 1:
            a += str(cnt)
        a += tmp

        answer = min(answer, len(a))
    return answer
