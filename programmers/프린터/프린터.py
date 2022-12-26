from collections import deque

def solution(priorities, location):
    answer = 1
    priorities = list(map(int, priorities))
    queue = deque(priorities)

    while queue:
        value = queue.popleft()

        if len(queue) == 0:
            return answer

        if value < max(queue):
            queue.append(value)
            if location == 0:
                location = len(queue)-1
            else:
                location -= 1
        else:
            if location == 0:
                return answer
            else:
                answer += 1
                location -= 1