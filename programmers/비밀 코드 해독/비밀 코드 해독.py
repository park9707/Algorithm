from itertools import combinations


def solution(n, q, ans):
    answer = 0
    m = len(q)
    not_secret_code = set()
    for i in range(m):
        if ans[i] == 0:
            not_secret_code.add(j for j in q[i])
        elif ans[i] == 5:
            return 1

    nums = [i for i in range(1, n + 1) if i not in not_secret_code]

    for combi in combinations(nums, 5):
        for i in range(m):
            cnt = 0
            for j in q[i]:
                if j in combi:
                    cnt += 1

            if ans[i] != cnt:
                break
        else:
            answer += 1

    return answer