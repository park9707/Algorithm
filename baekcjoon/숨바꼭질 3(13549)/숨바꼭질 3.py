import sys, collections
input = sys.stdin.readline

n, k = map(int, input().split())
q = collections.deque()
visited = [-1] * 100001
visited[n] = 0
q.append(n)

while q:
    x = q.popleft()

    next_x = x * 2
    if 0 <= next_x <= 100000 and visited[next_x] == -1 and abs(k - next_x) < (k - x):
        visited[next_x] = visited[x]
        q.appendleft(next_x)

    next_x = x - 1
    if 0 <= next_x and visited[next_x] == -1:
        visited[next_x] = visited[x] + 1
        q.append(next_x)

    next_x = x + 1
    if next_x <= 100000 and visited[next_x] == -1:
        visited[next_x] = visited[x] + 1
        q.append(next_x)

print(visited[k])
