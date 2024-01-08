from collections import defaultdict


def solution(edges):
    answer = [0] * 4
    wire = defaultdict(list)
    node = defaultdict(int)
    n = 0
    for a, b in edges:
        wire[a].append(b)
        node[b] += 1
        n = max(n, a, b)

    for i in range(1, n + 1):
        if len(wire[i]) > 1 and node[i] == 0:
            answer[0] = i
        elif not wire[i]:
            answer[2] += 1
        elif len(wire[i]) > 1 and node[i] > 1:
            answer[3] += 1

    answer[1] = len(wire[answer[0]]) - sum(answer[2:])

    return answer
