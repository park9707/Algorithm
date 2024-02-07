import heapq
from itertools import product


def solution(k, n, reqs):
    answer = float('inf')
    consulting = [[] for _ in range(k)]
    for a, b, c in reqs:
        consulting[c-1].append([a, b])
    waiting_times = [[0] * (n - k + 1) for _ in range(k)]

    for i in range(k):
        if not consulting[i]:
            continue
        for j in range(len(waiting_times[0])):
            consultant = j + 1
            start_q = consulting[i].copy()
            heapq.heapify(start_q)
            end_q = []
            now = start_q[0][0]
            waiting_t = 0
            while start_q:
                if consultant:
                    start_t, end_t = heapq.heappop(start_q)
                    waiting_t += max((now - start_t), 0)
                    heapq.heappush(end_q, max(start_t, now) + end_t)
                    consultant -= 1
                else:
                    now = heapq.heappop(end_q)
                    consultant += 1

            waiting_times[i][j] = max(0, waiting_t)
            if waiting_t == 0:
                break

    for p in product(range(1, n - k + 2), repeat=k):
        if sum(p) == n:
            temp = 0
            for i, num in enumerate(p):
                temp += waiting_times[i][num-1]
            answer = min(answer, temp)

    return answer
