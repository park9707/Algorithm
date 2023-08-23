import sys
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(r)]


def dfs(x, y):
    if y == c-1:
        return True

    for dx in range(-1, 2):
        nx = x + dx
        ny = y + 1

        if 0 <= nx < r and ny < c and maps[nx][ny] == '.':
            maps[nx][ny] = 'x'
            if dfs(nx, ny):
                return True
    return False


answer = 0
for start in range(r):
    if dfs(start, 0):
        answer += 1

print(answer)
