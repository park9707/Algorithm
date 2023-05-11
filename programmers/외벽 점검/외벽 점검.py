from collections import deque
from itertools import permutations


def check(dif, d):
    q = deque(dif)
    length = len(dif) - 1
    for a in permutations(d):
        c = 0
        while c <= length:
            i = -1
            for b in a:
                i += 1
                while i < length and b - q[i] >= 0:
                    b -= q[i]
                    i += 1

            if i == length:
                return True

            q.append(q.popleft())
            c += 1
    return False


def solution(n, weak, dist):
    dif = []
    for i in range(len(weak)):
        d = min(abs(weak[i] - weak[i - 1]), abs(weak[i] + n - weak[i-1]), abs(weak[i-1] + n - weak[i]))
        dif.append(d)

    for i in range(len(dist) - 1, -1, -1):
        if check(dif, dist[i:]):
            return len(dist) - i
    return -1
