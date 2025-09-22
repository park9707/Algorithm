import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
conveyor_belt = deque(list(map(int, input().split())))
step = 0
robot = deque([False] * n)

while True:
    step += 1
    conveyor_belt.rotate(1)
    robot.rotate(1)
    robot[-1] = False

    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i + 1] and conveyor_belt[i + 1] > 0:
            robot[i + 1] = robot[i]
            robot[i] = False
            conveyor_belt[i + 1] -= 1
            if not conveyor_belt[i + 1]:
                k -= 1
    robot[-1] = False

    if conveyor_belt[0] and not robot[0]:
        robot[0] = True
        conveyor_belt[0] -= 1
        if conveyor_belt[0] == 0:
            k -= 1

    if k <= 0:
        break

print(step)