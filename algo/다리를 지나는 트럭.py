# 다리에는 트럭이 bridge_length 개수 만큼올라갈 수 있음,  
# 다리는 weight 이하까지의 무게를 견딜 수 있다. 
# 단 다리에 완전히 오르지 않은 트럭의 무게는 무시 

# 1 (7, 1)
# 2 (7, 1)
# 3 (4, 3)
# 4 (4, 3), (5, 4)
# 5 (5, 4)
# 6 (6, 6)
# 7 (6, 6)
# 8 

# 한 번에 하나의 트럭만 올라갈 수 있나 ?? 아직 트럭이 내리지 않았다면 
# 즉, 1초에 타거나 내리는 경우가, 타기만 하는 경우, 내리기만 하는 경우가 있을 수 있겠다. 
# time을 기준으로 돌릴 것 같아 무한으로 
# 종료 조건은 대기트럭 수가 없고, 다리를 건너는 트럭이 없다면 종료해야할 것 같음 
# 큐에는 무게와 입장한 시간을 넣을 것임
# 1초마다 

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    truck_list = deque(truck_weights)
    curr_bridge_status = deque()
    curr_bridge_wegiht = 0
    
    while truck_list or curr_bridge_status :
        
        if curr_bridge_status and curr_bridge_status[0][1] + bridge_length == time :
            # 다리에서 내려야 하는 경우이므로 현재 다리의 무게를 감소시켜 줌 
            curr_bridge_wegiht -= curr_bridge_status.popleft()[0]
        
        if truck_list and curr_bridge_wegiht + truck_list[0] <= weight :
            # 다리에 올라갈 수 있음
            truck_weight = truck_list.popleft()
            curr_bridge_wegiht += truck_weight
            curr_bridge_status.append((truck_weight, time))
            
        time += 1
    
    return time 