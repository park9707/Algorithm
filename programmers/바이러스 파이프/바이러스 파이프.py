from itertools import product
from collections import defaultdict


def solution(n, infection, edges, k):
    ans = 0
    pipe = [[] for _ in range(n + 1)]
    for a, b, c in edges:
        pipe[a].append([b, c])
        pipe[b].append([a, c])

    for permutation in product(range(1, 4), repeat=k):
        types = defaultdict(list)
        for b, c in pipe[infection]:
            types[c].append(b)

        visited = [0] * (n + 1)
        visited[infection] = 1

        for opened_pipe in permutation:
            while types[opened_pipe]:
                node = types[opened_pipe].pop()
                if visited[node] == 0:
                    visited[node] = 1
                    for next_node, next_pipe in pipe[node]:
                        types[next_pipe].append(next_node)

        ans = max(ans, sum(visited))

    return ans