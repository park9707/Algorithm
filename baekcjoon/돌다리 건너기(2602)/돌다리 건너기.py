import sys
input = sys.stdin.readline


def cross(now):
    pos = set()
    next_bridge = now ^ 1
    for i in range(m):
        if bridge[i][now] == scroll[0]:
            pos.add(i)
            dp[0][i][now] = 1

    for i in range(1, n):
        next_pos = set()
        target = scroll[i]
        for j in pos:
            for k in range(j+1, m):
                if bridge[k][next_bridge] == target:
                    next_pos.add(k)
                    dp[i][k][next_bridge] += dp[i-1][j][next_bridge ^ 1]

        pos = next_pos
        next_bridge ^= 1

    return sum([dp[n-1][p][next_bridge ^ 1] for p in pos])


scroll = list(input().rstrip())
devil = list(input().rstrip())
angel = list(input().rstrip())
n, m = len(scroll), len(devil)
bridge = [[devil[i], angel[i]] for i in range(m)]
dp = [[[0, 0] for _ in range(m)] for _ in range(n)]

print(cross(0) + cross(1))