from collections import deque


def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    answer = 0
    limit = len(queue1) * 2 +2
    q1 = sum(queue1)
    q2 = sum(queue2)
    while q1 != q2:
        if answer == limit:
            return -1
        if q1 > q2:
            v = queue1.popleft()
            queue2.append(v)
            q1 -= v
            q2 += v
            answer += 1
        else:
            v = queue2.popleft()
            queue1.append(v)
            q1 += v
            q2 -= v
            answer += 1

    return answer