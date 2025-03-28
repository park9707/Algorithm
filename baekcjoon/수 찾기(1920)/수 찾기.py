import sys
input = sys.stdin.readline

n = int(input())
dic = dict()
nums = list(map(int, input().split()))
for num in nums:
    dic[num] = 1

m = int(input())
nums = list(map(int, input().split()))
for num in nums:
    print(dic.get(num, 0))
