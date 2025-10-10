import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    m = int(input())
    arr = []
    for _ in range((m + 9) // 10):
        arr += list(map(int, input().split()))
    ans = [arr[0]]
    left, right = [], []
    mid = arr[0]
    for i in range(1, m):
        num = arr[i]
        if num > mid:
            heapq.heappush(right, num)
        else:
            heapq.heappush(left, -num)

        if i % 2 == 0:
            if len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
            ans.append(mid)

    print(len(ans))
    for i in range((len(ans) + 9) // 10):
        print(*ans[10 * i: 10 * (i + 1)])
