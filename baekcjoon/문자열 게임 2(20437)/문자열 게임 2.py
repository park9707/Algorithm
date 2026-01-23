import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    w = input().rstrip()
    k = int(input())
    dic = defaultdict(list)

    for i in range(len(w)):
        dic[w[i]].append(i)

    min_length = 10000
    max_length = 0

    for c in dic:
        if len(dic[c]) < k:
            continue
        for i in range(len(dic[c]) - k + 1):
            length = dic[c][i + k - 1] - dic[c][i] + 1

            min_length = min(min_length, length)
            max_length = max(max_length, length)

    if min_length > max_length:
        print(-1)
    else:
        print(min_length, max_length)