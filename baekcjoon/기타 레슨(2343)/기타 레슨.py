import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lessons = list(map(int, input().split()))
start = max(lessons)
end = sum(lessons)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    t = 0
    for lesson in lessons:
        if t + lesson > mid:
            cnt += 1
            t = 0
        t += lesson

    if t > 0:
        cnt += 1

    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)