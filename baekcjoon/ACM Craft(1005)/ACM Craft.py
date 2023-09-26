import sys, collections
input = sys.stdin.readline


def topology_sort():
    result = []
    q = collections.deque()

    for i in range(1, n + 1):
        if node[i] == 0:
            q.append(i)
            dp[i] = cost[i]

    while q:
        now = q.popleft()
        result.append(now)
        for w in wire[now]:
            node[w] -= 1
            dp[w] = max(dp[w], dp[now] + cost[w])
            if node[w] == 0:
                q.append(w)

        if node[target] == 0:
            return dp[target]

    return result


t = int(input().rstrip())

for _ in range(t):
    n, k = map(int, input().rstrip().split())
    cost = [0] + list(map(int, input().rstrip().split()))
    dp = [0] * (n + 1)
    node = [0] * (n + 1)
    wire = [[] for _ in range(n + 1)]
    for _ in range(k):
        a, b = map(int, input().split())
        wire[a].append(b)
        node[b] += 1
    target = int(input().rstrip())

    print(topology_sort())
