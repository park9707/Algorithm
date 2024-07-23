import sys, collections
input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))
q = collections.deque([[0, arr[0]]])
print(arr[0], end=' ')

for i in range(1, n):
    if q[0][0] <= i - l:
        q.popleft()

    while q and q[-1][1] >= arr[i]:
        q.pop()

    q.append([i, arr[i]])

    print(q[0][1], end=' ')