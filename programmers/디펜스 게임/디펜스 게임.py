from heapq import heappush, heappushpop


def solution(n, k, enemy):
    heap = []
    for i in range(len(enemy)):
        if n >= enemy[i]:
            n -= enemy[i]
            heappush(heap, -enemy[i])
        elif k > 0:
            k -= 1
            n = n - heappushpop(heap, -enemy[i]) - enemy[i]
        else:
            return i
    return len(enemy)
