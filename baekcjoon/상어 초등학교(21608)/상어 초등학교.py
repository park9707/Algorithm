import sys, collections
input = sys.stdin.readline

N = int(input())
n = N * N
board = [[0] * N for _ in range(N)]
connection = [[0] * (n + 1) for _ in range(n + 1)]
empty = {(i, j): 4 for i in range(N) for j in range(N)}
for i in range(N):
    empty[0, i] -= 1
    empty[N-1, N-i-1] -= 1
    empty[i, 0] -= 1
    empty[N-i-1, N-1] -= 1
location = [[] for _ in range(n + 1)]
favorite = [[] for _ in range(n + 1)]
arr = []
move = ((-1, 0), (0, -1), (0, 1), (1, 0))

for _ in range(n):
    num, *students = list(map(int, input().split()))
    favorite[num].extend(students)
    arr.append(num)
board[1][1] = arr[0]
location[arr[0]] = [1, 1]
for x, y in [[0, 1], [1, 0], [2, 1], [1, 2]]:
    empty[x, y] -= 1

for i in arr[1:]:
    temp = collections.defaultdict(int)
    for j in favorite[i]:
        if location[j]:
            x, y = location[j]
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not board[nx][ny]:
                    temp[nx, ny] += 1
    print(temp)
    if temp:
        v = 0
        for tx, ty in sorted(temp.keys()):
            print(tx, ty)
            if temp[tx, ty] > v:
                x, y, v = tx, ty, temp[tx, ty]
            elif temp[tx, ty] == v and empty[tx, ty] > empty[x, y]:
                x, y = tx, ty
    else:
        x, y, v = N-1, N-1, -1
        for a, b in empty.keys():
            if empty[a, b] > v and not board[a][b]:
                x, y, v = a, b, empty[a, b]
                if v == 4:
                    break

    board[x][y] = i
    location[i] = [x, y]
    del empty[x, y]
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            connection[board[nx][ny]][i] = 1
            connection[i][board[nx][ny]] = 1
            print(empty)
            print(empty.get(nx, ny), nx, ny)
            print(empty.get(nx, ny))
            if empty.get(nx, ny):
                print(nx, ny)
                empty[nx, ny] -= 1
    print(board)

ans = 0
score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
for a in arr:
    num = sum(connection[a][p] for p in favorite[a])
    ans += score[num]

print(ans)