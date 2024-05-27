import sys, collections
input = sys.stdin.readline

S = list(input().rstrip())
T = collections.deque(input().rstrip())

n = len(T) - len(S)
is_reversed = False

for _ in range(n):
    if not is_reversed:
        if T[-1] == 'B':
            is_reversed = not is_reversed
        T.pop()
    else:
        if T[0] == 'B':
            is_reversed = not is_reversed
        T.popleft()

if is_reversed:
    T.reverse()

for a, b in zip(S, T):
    if a != b:
        print(0)
        break
else:
    print(1)
