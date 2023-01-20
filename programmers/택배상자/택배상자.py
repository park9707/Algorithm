from collections import deque
def solution(order):
    n = 0
    q = deque([0])
    i = 1
    while i <= len(order):
        if i != order[n] and q[0] != order[n]:
            q.appendleft(i)
            i += 1
        elif i == order[n]:
            n += 1
            i += 1
        elif q[0] == order[n]:
            q.popleft()
            n += 1

    while q[0] != 0:
        if order[n] == q[0]:
            q.popleft()
            n += 1
        else:
            return n
    return n