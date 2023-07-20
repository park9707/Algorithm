def solution(name):
    answer = 0
    n = len(name)
    cnt = n - 1

    for i, c in enumerate(name):
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)

        nxt = i + 1
        while nxt < n and name[nxt] == 'A':
            nxt += 1

        cnt = min(cnt, i * 2 + n - nxt, (n - nxt) * 2 + i)

    return answer + cnt
