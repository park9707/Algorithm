import sys, collections
input = sys.stdin.readline

n, d, k, c = map(int, input().rstrip().split())
sushi = [int(input().rstrip()) for _ in range(n)]
dic = collections.defaultdict(int)
for i in range(k):
    dic[sushi[i]] += 1
dic[c] += 1


def rotate(l, r, limit):
    global dic, sushi
    num = 0
    while r < limit:
        temp = sushi[l]
        dic[temp] -= 1
        dic[sushi[r]] += 1
        if dic[temp] < 1:
            del(dic[temp])
        l += 1
        r += 1
        num = max(num, len(dic.keys()))
    return num


answer = max(len(dic.keys()), rotate(0, k, n))
answer = max(answer, rotate(n-k, 0, k))

print(answer)
