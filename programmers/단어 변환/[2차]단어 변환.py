from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    q = deque([[begin, 0]])
    words = deque(words)
    while q:
        w, n = q.popleft()
        for _ in range(len(words)):
            word = words.popleft()
            cnt = 0
            for i in range(len(w)):
                if w[i] == word[i]:
                    continue
                else:
                    if cnt == 1:
                        words.append(word)
                        break
                    cnt += 1
            else:
                if word == target:
                    return n + 1
                q.append([word, n + 1])
    return 0
