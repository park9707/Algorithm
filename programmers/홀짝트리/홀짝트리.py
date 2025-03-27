from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)


def solution(nodes, edges):
    def check(n):
        visited[n] = True
        if (n % 2 == 1 and len(e[n]) % 2 == 0) or (n % 2 == 0 and len(e[n]) % 2 == 1):
            tr[0] += 1
        else:
            tr[1] += 1
        for next_n in e[n]:
            if not visited[next_n]:
                check(next_n)

    answer = [0, 0]
    e = defaultdict(list)
    visited = {i: False for i in nodes}
    for a, b in edges:
        e[a].append(b)
        e[b].append(a)

    for node in nodes:
        if not visited[node]:
            if len(e[node]) == 0:
                if node % 2 == 0:
                    answer[0] += 1
                else:
                    answer[1] += 1
                continue

            tr = [0, 0]
            check(node)

            if tr[0] == 1:
                answer[1] += 1
            if tr[1] == 1:
                answer[0] += 1

    return answer