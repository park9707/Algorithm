from collections import Counter


def solution(a):
    answer = 0
    n = len(a)
    dic = Counter(a)

    for key, value in dic.items():
        if value <= answer:
            continue
        i = 0
        cnt = 0
        while i < n - 1:
            if (a[i] == a[i + 1]) or (a[i] != key and a[i + 1] != key):
                i += 1
                continue

            cnt += 1
            i += 2

        answer = max(answer, cnt)

    return answer * 2
