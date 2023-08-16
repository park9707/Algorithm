import sys, itertools
input = sys.stdin.readline

n = int(input())
m = int(input())
dis = list(map(int, input().split()))
bt = [str(i) for i in range(10) if i not in dis]
length = len(list(str(n)))
answer = abs(100 - n)

for j in range(max(length - 1, 1), min(length + 2, 7)):
    for i in itertools.product(bt, repeat=j):
        answer = min(abs(int(''.join(i)) - n) + j, answer)

print(answer)