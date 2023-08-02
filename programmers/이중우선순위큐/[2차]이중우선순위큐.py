import heapq


def solution(operations):
    max_heap = []
    min_heap = []
    for c, n in [op.split() for op in operations]:
        n = int(n)
        if c == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
        elif c == 'D':
            if len(min_heap) == 0:
                continue
            elif n < 0:
                heapq.heappop(min_heap)
                max_heap.pop()
            elif n > 0:
                heapq.heappop(max_heap)
                min_heap.pop()

    return [0, 0] if not min_heap else [-max_heap[0], min_heap[0]]
