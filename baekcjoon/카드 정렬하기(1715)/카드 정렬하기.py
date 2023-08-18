import sys, heapq
input = sys.stdin.readline

n = int(input())
result = 0
nums = [int(input()) for _ in range(n)]
if n > 1:
    heapq.heapify(nums)
    cnt = len(nums)

    while cnt > 1:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        result += a + b
        heapq.heappush(nums, a + b)
        cnt -= 1

print(result)
