import heapq


def solution(book_time):
    answer = 0
    s_heap = []
    e_heap = []
    for s, e in book_time:
        s_time = (int(s[:2]) * 60) + int(s[3:])
        e_time = (int(e[:2]) * 60) + int(e[3:])

        heapq.heappush(s_heap, s_time)
        heapq.heappush(e_heap, e_time)

    room = 0

    while s_heap:
        s_time = heapq.heappop(s_heap)

        while e_heap[0] + 10 <= s_time:
            heapq.heappop(e_heap)
            room -= 1
        room += 1
        answer = max(answer, room)

    return answer