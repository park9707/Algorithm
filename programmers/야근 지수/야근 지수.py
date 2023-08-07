import heapq


def solution(n, works):
    if n >= sum(works):
        return 0

    heap = [-i for i in works]
    heapq.heapify(heap)
    for _ in range(n):
        num = heapq.heappop(heap)
        heapq.heappush(heap, num+1)

    return sum(m**2 for m in heap)
