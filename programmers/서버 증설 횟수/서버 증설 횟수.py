from collections import deque


def solution(players, m, k):
    server = deque()
    ans = 0
    for i, n in enumerate(players):
        if n == 0:
            continue
        while server and server[0] <= i:
            server.popleft()

        s = n // m
        if len(server) < s:
            ans += (s - len(server))
            [server.append(i + k) for _ in range(s - len(server))]
    return ans