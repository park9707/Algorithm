import heapq


def solution(n, works):
    if n >= sum(works):
        return 0

    heapq.heapify(heap := [-w for w in works])
    for _ in range(n):
        temp = heapq.heappop(heap)
        if temp != -1:
            heapq.heappush(heap, temp + 1)

    return sum(w ** 2 for w in heap)
