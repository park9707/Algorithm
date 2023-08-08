import sys, heapq
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))

result = ['0'] * (n + 1)
heap = [[top[-1], n]]

for i in range(2, n+1):
    top_h = top[-i]
    while heap and heap[0][0] < top_h:
        h, idx = heapq.heappop(heap)
        result[idx] = str(n-i+1)
    heapq.heappush(heap, [top_h, n-i+1])

print(" ".join(result[1:]))
