import sys
input = sys.stdin.readline


def update(idx):
    while idx > 0:
        tree[idx] = tree[idx * 2] * tree[idx * 2 + 1] % 1000000007
        idx //= 2


def multiply(left, right):
    result = 1
    while left <= right:
        if left % 2:
            result = (result * tree[left]) % 1000000007
            left += 1
        if right % 2 == 0:
            result = (result * tree[right]) % 1000000007
            right -= 1
        left //= 2
        right //= 2

    return result


n, m, k = map(int, input().split())
h = 1
while h < n:
    h *= 2

tree = [1] * (h * 2)
for i in range(n):
    tree[h + i] = int(input())
for i in range(h-1, 0, -1):
    tree[i] = tree[i * 2] * tree[i * 2 + 1] % 1000000007

for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        tree[h + b - 1] = c
        update((h + b - 1) // 2)
    elif a == 2:
        print(multiply(h + b - 1, h + c - 1))