import sys
input = sys.stdin.readline

matches = [0, 0, 1, 7, 4, 2, 6, 8] + [888888888888888] * 93

for i in range(8, 101):
    for j in range(2, i - 1):
        matches[i] = min(matches[i], int(str(matches[j]) + str(matches[i - j])))
    matches[i] = min(matches[i], int(str(matches[i - 6]) + '0'))

T = int(input())
for _ in range(T):
    n = int(input())
    print(matches[n], '1' * (n // 2) if n % 2 == 0 else '7' + ('1' * (n // 2 - 1)))