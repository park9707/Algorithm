from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 1
    truck_weights = deque(truck_weights)
    now_truck = deque([[truck_weights.popleft(), time]])
    weight -= now_truck[0][0]

    while truck_weights:
        time += 1

        if time - now_truck[0][1] == bridge_length:
            truck_weight, t = now_truck.popleft()
            weight += truck_weight

        if weight - truck_weights[0] >= 0:
            truck = truck_weights.popleft()
            now_truck.append([truck, time])
            weight -= truck

    return time + bridge_length