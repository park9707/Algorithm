import heapq

def solution(scoville, k):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    cnt = 0
    while heap[0] < k:
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        cnt += 1

        if len(heap) == 1 and heap[0] < k:
            return -1
    return cnt