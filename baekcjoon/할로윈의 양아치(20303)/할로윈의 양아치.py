import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())
candy = [0] + list(map(int, input().split()))
friend = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

visited = [False] * (N + 1)
cnt = []
for i in range(1, N + 1):
    if not visited[i]:
        arr = [i]
        friend_num = 1
        visited[i] = True
        while arr:
            n = arr.pop()
            for x in friend[n]:
                if not visited[x]:
                    visited[x] = True
                    candy[i] += candy[x]
                    friend_num += 1
                    arr.append(x)
        if friend_num < K:
            cnt.append([friend_num, candy[i]])

dp = [0] * K
for i, v in cnt:
    for j in range(K - 1, i - 1, -1):
        dp[j] = max(dp[j], dp[j-i] + v)

print(max(dp))