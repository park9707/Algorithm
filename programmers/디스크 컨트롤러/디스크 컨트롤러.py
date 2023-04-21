import heapq


def solution(jobs):
    jobs.sort(key=lambda x: (x[0], x[1]))
    answer = []
    heap = []
    n = len(jobs)
    i = 0
    t = jobs[i][0]
    while i < n:
        while i < n and jobs[i][0] <= t:
            heapq.heappush(heap, jobs[i][::-1])
            i += 1

        if not heap:
            heapq.heappush(heap, jobs[i][::-1])
            t = jobs[i][0]
            i += 1

        now = heapq.heappop(heap)
        answer.append(t - now[1] + now[0])
        t += now[0]

    while heap:
        now = heapq.heappop(heap)
        answer.append(t - now[1] + now[0])
        t += now[0]

    return sum(answer) // n
