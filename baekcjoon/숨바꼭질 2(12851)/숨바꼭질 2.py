import sys, collections
input = sys.stdin.readline

n, k = map(int, input().split())
if n >= k:
    print(n - k)
    print(1)
    exit()
max_d = k + 3
dp = [0] * max_d
visited = [0] * max_d
dp[n] = visited[n] = 1
q = collections.deque([n])

for i in range(1, k - n + 1):
    for _ in range(len(q)):
        num = q.popleft()
        cnt = dp[num]
        if max_d > num + 1:
            if visited[num + 1] == 0:
                dp[num + 1] += cnt
                visited[num + 1] = i
                q.append(num + 1)
            elif visited[num + 1] == i:
                dp[num + 1] += cnt

        if 0 <= num - 1:
            if visited[num - 1] == 0:
                dp[num - 1] += cnt
                visited[num - 1] = i
                q.append(num - 1)
            elif visited[num - 1] == i:
                dp[num - 1] += cnt

        if max_d > num * 2:
            if visited[num * 2] == 0:
                dp[num * 2] += cnt
                visited[num * 2] = i
                q.append(num * 2)
            elif visited[num * 2] == i:
                dp[num * 2] += cnt

    if dp[k]:
        break

print(i)
print(dp[k])
