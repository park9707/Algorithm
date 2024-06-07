import sys
input = sys.stdin.readline

N = int(input())
buildings = list(map(int, input().split()))
ans = 0

for i in range(N):
    temp = N - 1
    for j in range(i + 1, N):
        for k in range(i + 1, j):
            if buildings[k] - buildings[i] >= (((buildings[j] - buildings[i]) / (j - i)) * (k - i)):
                temp -= 1
                break

    for j in range(i):
        for k in range(j + 1, i):
            if buildings[k] - buildings[j] >= (((buildings[i] - buildings[j]) / (i - j)) * (k - j)):
                temp -= 1
                break

    ans = max(temp, ans)

print(ans)