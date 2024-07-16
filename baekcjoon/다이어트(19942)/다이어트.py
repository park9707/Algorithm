import sys
sys.setrecursionlimit(10**6)
input = sys.stdin. readline


def backtracking(nums, cost, p, f, s, v):
    global min_cost
    if cost >= min_cost:
        return

    if p >= mp and f >= mf and s >= ms and v >= mv:
        global ans
        ans = [n + 1 for n in nums]
        min_cost = cost
        return

    for k in range(nums[-1] + 1, N):
        tp, tf, ts, tv, tc = foods[k]
        nums.append(k)
        backtracking(nums, cost + tc, p + tp, f + tf, s + ts, v + tv)
        nums.pop()


N = int(input())
mp, mf, ms, mv = map(int, input().split())
foods = [list(map(int, input().split())) for _ in range(N)]
min_cost = float('inf')
ans = []
for i in range(N):
    p, f, s, v, c = foods[i]
    backtracking([i], c, p, f, s, v)

if min_cost == float('inf'):
    print(-1)
    exit()

print(min_cost)
print(*ans)
