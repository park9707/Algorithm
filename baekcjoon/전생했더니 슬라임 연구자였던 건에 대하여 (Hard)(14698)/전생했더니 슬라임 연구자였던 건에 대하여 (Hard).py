import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    slimes = list(map(int, input().split()))
    ans = 1
    heapq.heapify(slimes)
    for _ in range(n - 1):
        a = heapq.heappop(slimes)
        b = heapq.heappop(slimes)
        result = a * b
        ans = ans * result % 1000000007
        heapq.heappush(slimes, result)

    print(ans % 1000000007)