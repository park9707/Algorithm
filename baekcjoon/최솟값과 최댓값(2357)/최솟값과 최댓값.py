import sys
input = sys.stdin.readline

n, m = map(int, input().split())
h = 2
while h < n:
    h *= 2

tree = [[float('inf'), float('-inf')] for _ in range(h * 2)]
for i in range(n):
    temp = int(input())
    tree[h+i] = [temp, temp]

for i in range(h - 1, 0, -1):
    tree[i] = [min(tree[i * 2][0], tree[i * 2 + 1][0]), max(tree[i * 2][1], tree[i * 2 + 1][1])]

for _ in range(m):
    a, b = map(int, input().split())
    a += h - 1
    b += h - 1
    result = [float('inf'), float('-inf')]
    while a <= b:
        if a % 2 == 1:
            result[0] = min(result[0], tree[a][0])
            result[1] = max(result[1], tree[a][1])
            a += 1
        if b % 2 == 0:
            result[0] = min(result[0], tree[b][0])
            result[1] = max(result[1], tree[b][1])
            b -= 1

        a //= 2
        b //= 2

    print(*result)