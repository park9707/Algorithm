from collections import deque


def solution(begin, target, words):
    visited = [0] * len(words)
    q = deque()

    def bfs(q):
        while q:
            n = q.popleft()
            for i in range(len(words)):
                if visited[i] > 0:
                    continue
                cnt = 0
                for j in range(len(words[n])):
                    if words[n][j] != words[i][j]:
                        cnt += 1
                        if cnt > 1:
                            break
                else:
                    q.append(i)
                    visited[i] = visited[n] + 1

    a = -1
    for i in range(len(words)):
        if words[i] == target:
            a = i
        cnt = 0
        for j in range(len(begin)):
            if begin[j] != words[i][j]:
                cnt += 1
                if cnt > 1:
                    break
        else:
            q.append(i)
            visited[i] = 1
    bfs(q)
    return visited[a] if a != -1 else 0
