import sys, collections
input = sys.stdin.readline

n, k = map(int, input().split())
if k <= n:
    print(n - k)
    print(*list(range(n, k-1, -1)))
    exit()
max_d = k + 3
parents = [i for i in range(max_d)]
parents[k] = -1
q = collections.deque([k])

for i in range(k):
    for _ in range(len(q)):
        num = q.popleft()
        if max_d > num + 1:
            if parents[num + 1] == num + 1:
                parents[num + 1] = num
                q.append(num + 1)

        if 0 <= num - 1:
            if parents[num - 1] == num - 1:
                parents[num - 1] = num
                q.append(num - 1)

        if num % 2 == 0:
            if parents[num // 2] == num // 2:
                parents[num // 2] = num
                q.append(num // 2)

    if parents[n] != n:
        break

ans = [n]
while parents[n] != -1:
    n = parents[n]
    ans.append(n)

print(i + 1)
print(*ans)
