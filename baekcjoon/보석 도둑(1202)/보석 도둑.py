import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
jewel = sorted([list(map(int, input().rstrip().split())) for _ in range(n)])
bags = sorted([int(input().rstrip()) for _ in range(k)])
temp = []
ans = 0

for bag in bags:
    while jewel and bag >= jewel[0][0]:
        heapq.heappush(temp, -heapq.heappop(jewel)[1])
    if temp:
        ans -= heapq.heappop(temp)
    elif not jewel:
        break

print(ans)