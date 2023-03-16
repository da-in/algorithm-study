from collections import deque
def solution(bridge_length, weight, truck_weights):

    total_time = 0
    sum_weight = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)

    while bridge:
      
        total_time += 1
        sum_weight -= bridge[0]
        bridge.popleft()

        if truck_weights:
            if sum_weight + truck_weights[0] <= weight:
                sum_weight += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
                
    return total_time
