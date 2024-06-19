import sys, heapq, collections
input = sys.stdin.readline

N = int(input())
min_q = []
max_q = []
d = collections.defaultdict(dict)
for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(min_q, [L, P])
    heapq.heappush(max_q, [-L, -P])
    d[P][L] = True

M = int(input())
for i in range(M):
    command = list(input().rstrip().split())
    if command[0] == 'recommend':
        temp = False
        if command[1] == '-1':
            while not temp:
                L, P = heapq.heappop(min_q)
                temp = d[P].get(L, False)
            heapq.heappush(min_q, [L, P])
            print(P)
        else:
            while not temp:
                L, P = heapq.heappop(max_q)
                temp = d[-P].get(-L, False)
            heapq.heappush(max_q, [L, P])
            print(-P)
    elif command[0] == 'add':
        P, L = int(command[1]), int(command[2])
        heapq.heappush(min_q, [L, P])
        heapq.heappush(max_q, [-L, -P])
        d[P][L] = True
    else:
        del d[int(command[1])]
