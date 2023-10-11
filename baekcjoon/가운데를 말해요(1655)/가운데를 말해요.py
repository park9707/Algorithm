import sys, heapq
input = sys.stdin.readline

n = int(input().rstrip())
num = int(input().rstrip())
print(num)
min_q = []
max_q = [-num]

for _ in range(n-1):
    num = int(input().rstrip())
    if len(min_q) == len(max_q):
        heapq.heappush(max_q, -num)
    else:
        heapq.heappush(min_q, num)

    if -max_q[0] > min_q[0]:
        max_num = heapq.heappop(max_q)
        min_num = heapq.heappop(min_q)

        heapq.heappush(max_q, -min_num)
        heapq.heappush(min_q, -max_num)

    print(-max_q[0])
