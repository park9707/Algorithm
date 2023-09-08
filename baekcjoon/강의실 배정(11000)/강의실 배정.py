import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    start, end = map(int, input().rstrip().split())
    arr.append([start, 2])
    arr.append([end, 1])

arr.sort(key=lambda x: (x[0], x[1]))
room = 0
answer = 0

for time, num in arr:
    if num == 2:
        room += 1
        answer = max(answer, room)
    else:
        room -= 1

print(answer)
