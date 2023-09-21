import sys, heapq
input = sys.stdin.readline


def sync(q):
    while q and not check[q[0][1]]:
        heapq.heappop(q)


t = int(input().rstrip())

for _ in range(t):
    k = int(input().rstrip())
    min_q = []
    max_q = []
    n = 0
    check = [1] * k
    for i in range(k):
        command, num = input().rstrip().split()
        if command == 'I':
            heapq.heappush(min_q, [int(num), i])
            heapq.heappush(max_q, [-int(num), i])

        elif command == 'D':
            if num == '-1':
                sync(min_q)
                if min_q:
                    check[heapq.heappop(min_q)[1]] = 0
            elif num == '1':
                sync(max_q)
                if max_q:
                    check[heapq.heappop(max_q)[1]] = 0

    sync(min_q)
    sync(max_q)
    if min_q:
        print(-max_q[0][0], min_q[0][0])
    else:
        print('EMPTY')
