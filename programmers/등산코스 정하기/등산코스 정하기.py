import heapq


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    is_summit = [False] * (n + 1)
    dist = [0] + [10000001] * n

    for a, b, c in paths:
        graph[a].append([b, c])
        graph[b].append([a, c])

    for summit in summits:
        is_summit[summit] = True

    def dijkstra():
        q = []
        for gate in gates:
            heapq.heappush(q, [0, gate])
            dist[gate] = 0
        summit_list = []
        while q:
            d, now = heapq.heappop(q)

            if is_summit[now]:
                summit_list.append([now, d])
                if q and q[0][0] > d:
                    return summit_list
                continue

            for i in graph[now]:
                tmp_d = max(d, i[1])

                if dist[i[0]] <= tmp_d:
                    continue

                dist[i[0]] = tmp_d
                heapq.heappush(q, [tmp_d, i[0]])

        return summit_list

    answer = dijkstra()

    return sorted(answer, key=lambda x: (x[1], x[0]))[0]
