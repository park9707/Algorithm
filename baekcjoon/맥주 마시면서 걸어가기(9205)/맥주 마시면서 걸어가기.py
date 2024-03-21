import sys, collections
input = sys.stdin.readline


def bfs():
    n = int(input())
    q = collections.deque([list(map(int, input().split()))])
    store = [list(map(int, input().split())) for _ in range(n)]
    end_x, end_y = map(int, input().split())
    while q:
        x, y = q.popleft()

        if abs(x - end_x) + abs(y - end_y) <= 1000:
            return "happy"

        for i in range(len(store) - 1, -1, -1):
            nx, ny = store[i]
            if abs(nx - x) + abs(ny - y) <= 1000:
                q.append([nx, ny])
                store.pop(i)

    return "sad"


for _ in range(int(input())):
    print(bfs())
