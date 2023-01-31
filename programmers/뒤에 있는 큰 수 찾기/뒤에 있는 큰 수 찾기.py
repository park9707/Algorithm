from collections import deque

def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    q = deque()
    for i in range(n):
        value = numbers[i]

        while q and q[0][0] < value:
            _, idx = q.popleft()
            answer[idx] = value

        q.appendleft([value, i])

    return answer