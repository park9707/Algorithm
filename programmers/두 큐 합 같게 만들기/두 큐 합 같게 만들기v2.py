from collections import deque


def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum_a = sum(q1)
    sum_b = sum(q2)
    n = len(q1) * 2 + 1
    i = 0

    while i <= n:
        while sum_a > sum_b and i <= n:
            tmp = q1.popleft()
            q2.append(tmp)
            sum_a -= tmp
            sum_b += tmp
            i += 1

        while sum_b > sum_a and i <= n:
            tmp = q2.popleft()
            q1.append(tmp)
            sum_b -= tmp
            sum_a += tmp
            i += 1

        if sum_b == sum_a:
            return i

    return i if i <= n else -1