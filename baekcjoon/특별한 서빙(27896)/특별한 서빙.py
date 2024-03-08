import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
q = []
ans = 0
for num in arr:
    M -= num
    heapq.heappush(q, -num)
    if M <= 0:
        ans += 1
        M -= heapq.heappop(q) * 2

print(ans)