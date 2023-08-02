import heapq


def solution(operations):
    heap = []
    for c, n in [op.split() for op in operations]:
        n = int(n)
        if c == 'I':
            heapq.heappush(heap, n)
        elif c == 'D':
            if not heap:
                continue
            elif n < 0:
                heapq.heappop(heap)
            elif n > 0:
                heap.remove(max(heap))

    return [0, 0] if not heap else [max(heap), heap[0]]
