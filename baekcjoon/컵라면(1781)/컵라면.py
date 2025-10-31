import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[0], -x[1]))
q = []

for deadline, cup_ramen in arr:
    heapq.heappush(q, cup_ramen)
    if len(q) > deadline:
        heapq.heappop(q)

print(sum(q))