import heapq


def solution(n, k, enemy):
    heap = enemy[:k]
    heapq.heapify(heap)
    for i in range(k, len(enemy)):
        heapq.heappush(heap, enemy[i])
        enemy_num = heapq.heappop(heap)
        if n >= enemy_num:
            n -= enemy_num
        else:
            return i
    return len(enemy)
