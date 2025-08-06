import sys
input = sys.stdin.readline


def solution(buildings):
    arr = []
    for i, h in buildings:
        while arr and arr[-1][0] <= h:
            arr.pop()

        ans[i][0] += len(arr)

        if arr and abs(arr[-1][1] - i) < abs(ans[i][1] - i):
            ans[i][1] = arr[-1][1]

        arr.append([h, i])


n = int(input())
buildings = list(enumerate(map(int, input().split()), start=1))
ans = [[0, 200000] for _ in range(n + 1)]

solution(buildings)
solution(buildings[::-1])

for i in range(1, n + 1):
    print(*ans[i]) if ans[i][0] != 0 else print(0)