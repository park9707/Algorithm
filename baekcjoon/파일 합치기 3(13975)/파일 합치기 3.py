import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    heapq.heapify(q)
    ans = 0
    for _ in range(n - 2):
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        ans += a + b
        heapq.heappush(q, a + b)

    print(ans + sum(q))
