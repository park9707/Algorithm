n = int(input())
cnt = 0

while n > 0:
    if n % 5 == 0:
        print(n // 5 + cnt)
        break
    n -= 3
    cnt += 1

else:
    if n < 0:
        print(-1)
    else:
        print(cnt)