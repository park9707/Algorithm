n=int(input())
p=list(map(int,input().split()))
p.sort()

min_time=0

for i in range(1, n+1):
    min_time+=sum(p[0:i])

print(min_time)
