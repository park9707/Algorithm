from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck_weights = deque(truck_weights)
    trucks = deque([(truck_weights.popleft(), answer)])
    now_weight = trucks[0][0]
    
    while truck_weights:
        answer += 1

        if trucks[0][1] == answer - bridge_length:
            truck_weight, time = trucks.popleft()
            now_weight -= truck_weight

        if weight >= now_weight + truck_weights[0]:
            truck = truck_weights.popleft()
            now_weight += truck
            trucks.append((truck, answer))

    answer += bridge_length
    return answer