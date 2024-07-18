import sys, collections
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a_dic = collections.defaultdict(list)
b_dic = collections.defaultdict(list)

for i in range(n):
    num = a[i]
    a_dic[num].append(i)

for i in range(m):
    num = b[i]
    if a_dic.get(num, 0):
        b_dic[num].append(i)

i = j = -1
ans = []

for k in sorted(b_dic.keys(), reverse=True):
    arr1, arr2 = a_dic[k], b_dic[k]
    a_i = b_i = 0

    while a_i < len(arr1) and i > arr1[a_i]:
        a_i += 1

    while b_i < len(arr2) and j > arr2[b_i]:
        b_i += 1

    min_idx = min(len(arr1) - a_i, len(arr2) - b_i)
    if min_idx > 0:
        ans.extend([k] * min_idx)
        i = arr1[a_i + min_idx - 1]
        j = arr2[b_i + min_idx - 1]

print(len(ans))
print(*ans)
