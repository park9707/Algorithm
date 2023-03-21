import heapq


def solution(operations):
    max_heap = []
    min_heap = []
    for i in operations:
        if i[0] == 'I':
            num = int(i[2:])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-num, num))
        elif i[0] == 'D':
            if len(min_heap) == 0:
                continue
            elif i[2] == '-':
                heapq.heappop(min_heap)
                max_heap.pop()
            else:
                heapq.heappop(max_heap)
                min_heap.pop()

    if len(min_heap) == 0:
        return [0, 0]
    else:
        return [max_heap[0][1], min_heap[0]]
