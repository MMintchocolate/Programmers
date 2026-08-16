from collections import deque

def solution(bridge_length, weight, truck_weights):
    ing = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    total_weight = 0
    answer = 0
    while truck_weights or any(ing):
        answer+=1
        total_weight-=ing.popleft()
        
        if truck_weights and total_weight + truck_weights[0] <= weight:
            new = truck_weights.popleft()
            total_weight+=new
            ing.append(new)
        else:
            ing.append(0)

    return answer