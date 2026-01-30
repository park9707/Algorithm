import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = int(b ** 0.5) + 1
is_prime_num = [True] * c
ans = 0

for i in range(2, c):
    if is_prime_num[i]:
        for j in range(i + i, c, i):
            is_prime_num[j] = False

for i in range(2, c):
    if is_prime_num[i]:
        num = i * i
        while num <= b:
            if num >= a:
                ans += 1
            num *= i
print(ans)