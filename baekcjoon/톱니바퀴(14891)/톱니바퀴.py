import sys
from collections import deque
input = sys.stdin.readline


def q0_rotation(d0):
    right_rotation = False
    visited[0] = True
    if q0[2] ^ q1[6]:
        right_rotation = True

    if d0 == 1:
        q0.appendleft(q0.pop())
    else:
        q0.append(q0.popleft())

    if right_rotation and not visited[1]:
        q1_rotation(d0 * -1)


def q1_rotation(d1):
    left_rotation, right_rotation = False, False
    visited[1] = True
    if q1[6] ^ q0[2]:
        left_rotation = True
    if q1[2] ^ q2[6]:
        right_rotation = True

    if d1 == 1:
        q1.appendleft(q1.pop())
    else:
        q1.append(q1.popleft())

    if left_rotation and not visited[0]:
        q0_rotation(d1 * -1)
    if right_rotation and not visited[2]:
        q2_rotation(d1 * -1)


def q2_rotation(d2):
    left_rotation, right_rotation = False, False
    visited[2] = True
    if q2[6] ^ q1[2]:
        left_rotation = True
    if q2[2] ^ q3[6]:
        right_rotation = True

    if d2 == 1:
        q2.appendleft(q2.pop())
    else:
        q2.append(q2.popleft())

    if left_rotation and not visited[1]:
        q1_rotation(d2 * -1)
    if right_rotation and not visited[3]:
        q3_rotation(d2 * -1)


def q3_rotation(d3):
    left_rotation = False
    visited[3] = True
    if q3[6] ^ q2[2]:
        left_rotation = True

    if d3 == 1:
        q3.appendleft(q3.pop())
    else:
        q3.append(q3.popleft())

    if left_rotation and not visited[2]:
        q2_rotation(d3 * -1)


q0 = deque(list(map(int, input().rstrip())))
q1 = deque(list(map(int, input().rstrip())))
q2 = deque(list(map(int, input().rstrip())))
q3 = deque(list(map(int, input().rstrip())))
for _ in range(int(input())):
    n, d = map(int, input().split())
    visited = [False] * 4
    if n == 1:
        q0_rotation(d)
    elif n == 2:
        q1_rotation(d)
    elif n == 3:
        q2_rotation(d)
    else:
        q3_rotation(d)

print(int(''.join(map(str, [q3[0], q2[0], q1[0], q0[0]])), 2))