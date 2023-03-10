from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = list(reversed(truck_weights))
    current_weight = 0
    answer = 0
    while truck_weights:
        current_weight -= bridge.popleft()
        answer += 1
        if current_weight + truck_weights[-1] <= weight:
            truck = truck_weights.pop()
        else:
            truck = 0
        current_weight += truck
        bridge.append(truck)
    return answer + bridge_length
