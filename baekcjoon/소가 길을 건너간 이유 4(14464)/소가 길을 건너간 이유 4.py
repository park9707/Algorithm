import sys, heapq
input = sys.stdin.readline

C, N = map(int, input().split())
chickens = sorted([int(input()) for _ in range(C)])
cows = sorted([list(map(int, input().split())) for _ in range(N)])
temp = list()
i = j = ans = 0

for i in range(C):
    while j < N:
        s, e = cows[j]
        if s <= chickens[i]:
            heapq.heappush(temp, (e, s))
            j += 1
        else:
            break
    while temp:
        ee, ss = heapq.heappop(temp)
        if ss <= chickens[i] <= ee:
            ans += 1
            break

print(ans)