import sys
input = sys.stdin.readline

n = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)

if crane[0] < boxes[0]:
    print(-1)
    exit()

position = list(range(n))
moved = [False] * m
cnt = 0
ans = 0

while cnt < m:
    for i, capa in enumerate(crane):
        pos = position[i]
        for j in range(pos, m):
            if not moved[j] and boxes[j] <= capa:
                moved[j] = True
                position[i] = j + 1
                cnt += 1
                break
        else:
            crane = crane[:i + 1]
            break
    ans += 1
print(ans)