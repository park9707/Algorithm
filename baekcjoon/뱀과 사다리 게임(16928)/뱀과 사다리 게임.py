import sys, collections
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = [i for i in range(101)]
for _ in range(n + m):
    a, b = map(int, input().rstrip().split())
    board[a] = b


def bfs():
    q = collections.deque([[0, 1]])
    board[1] = 0
    while q:
        cnt, now = q.popleft()

        for i in range(1, 7):
            nx = now + i
            if 1 <= nx <= 100:
                next_n = board[nx]
                if next_n == 100:
                    return cnt + 1

                if board[next_n]:
                    board[next_n] = 0
                    q.append([cnt + 1, next_n])


print(bfs())
