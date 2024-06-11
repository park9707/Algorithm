import sys, heapq
input = sys.stdin.readline


def dijkstra(start):
    q = [[0, start]]
    distance = [float('inf')] * (n + 1)
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        for next_node, c in board[node]:
            cost = dist + c
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, [cost, next_node])

    return distance


T = int(input())
for _ in range(T):
    # n: 노드 수, m: 도로 개수, t: 도착지 후보 수
    n, m, t = map(int, input().split())
    # s: 출발 지점, g, h: 이 사이의 도로를 무조건 건넘
    s, g, h = map(int, input().split())
    board = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        board[a].append([b, d])
        board[b].append([a, d])
    candidate_site = [int(input()) for _ in range(t)]

    arr1 = dijkstra(s)
    if arr1[g] < arr1[h]:
        new_start = h
    else:
        new_start = g
    arr2 = dijkstra(new_start)
    ans = []

    for i in candidate_site:
        if arr1[i] == arr1[new_start] + arr2[i] and arr1[i] != float('inf'):
            ans.append(i)
    ans.sort()
    print(*ans)
