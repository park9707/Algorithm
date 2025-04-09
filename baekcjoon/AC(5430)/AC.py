import sys, collections
input = sys.stdin.readline

for _ in range(int(input())):
    p = list(input().rstrip())
    n = int(input())
    nums = collections.deque(input().rstrip()[1:-1].split(',') if n != 0 else input().rstrip()[1:-1])
    r = 1
    for i in range(len(p)):
        if p[i] == 'R':
            r *= -1
        else:
            if not nums:
                print('error')
                break
            if r == 1:
                nums.popleft()
            else:
                nums.pop()
    else:
        if r == 1:
            print("[" + ",".join(nums) + "]")
        else:
            print("[" + ",".join(reversed(nums)) + "]")