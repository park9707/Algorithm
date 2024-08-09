import sys
input = sys.stdin.readline

n,k = map(int,input().split())

start = 0
digit = 1
nine = 9

while k > nine*digit :
  k = k - ( digit * nine )
  start = start + nine
  nine = nine*10
  digit += 1

result = (start+1) + (k-1)//digit

if result > n:
    print(-1)
else:
    print(str(result)[(k-1) % digit])
