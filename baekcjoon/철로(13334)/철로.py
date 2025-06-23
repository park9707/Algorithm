import sys
import heapq
input = sys.stdin.readline

n = int(input())
location = [list(sorted(map(int, input().split()))) for _ in range(n)]
d = int(input())
location.sort(key=lambda x: (x[1], x[0]))

q = []
ans = 0

for start, end in location:
    heapq.heappush(q, start)
    rail_start = end - d
    while q and q[0] < rail_start:
        heapq.heappop(q)
    ans = max(ans, len(q))

print(ans)