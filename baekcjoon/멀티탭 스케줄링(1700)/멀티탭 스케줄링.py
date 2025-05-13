import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = list(map(int, input().split()))
code = dict()
ans = 0

for i in range(k):
    if code.get(items[i], False):
        continue

    if len(code) < n:
        code[items[i]] = True
        continue

    tmp = [0, 0]
    for c in code.keys():
        for j in range(i + 1, k):
            if items[j] == c:
                if j > tmp[0]:
                    tmp = [j, items[j]]
                break
        else:
            tmp = [0, c]
            break
    del code[tmp[1]]
    code[items[i]] = True
    ans += 1

print(ans)
