import sys
input = sys.stdin.readline


def check(l, r, c):
    building = [[] for _ in range(l)]
    sz = sx = sy = ez = ex = ey = 0
    for z in range(l):
        for x in range(r):
            building[z].append(list(input().rstrip()))
            for y in range(c):
                if building[z][x][y] == 'S':
                    sz, sx, sy = z, x, y
                    building[z][x][y] = '#'

                elif building[z][x][y] == 'E':
                    ez, ex, ey = z, x, y
        _ = input()
    stack = [[sz, sx, sy]]
    ans = 0
    while stack:
        ans += 1
        new_stack = []
        for i in range(len(stack)):
            z, x, y = stack[i]

            for dz, dx, dy in move:
                nz = z + dz
                nx = x + dx
                ny = y + dy

                if nz == ez and nx == ex and ny == ey:
                    return 'Escaped in ' + str(ans) + ' minute(s).'

                if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                    if building[nz][nx][ny] != '#':
                        building[nz][nx][ny] = '#'
                        new_stack.append([nz, nx, ny])
        stack = new_stack
    return 'Trapped!'


move = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))
while True:
    l, r, c = map(int, input().split())
    if l == r == c == 0:
        break

    print(check(l, r, c))