


from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    truck_weights = deque(truck_weights)
    
    # 튜플을 저장 (들어간 시간, 현재 트럭 무게)
    bridgeInTrucks = deque()
    bridgeInTrucksWeight = 0
    currentTime = 0 
    
    # 모든 트럭이 다리에 진입했고, 모든 트럭이 다리를 지나지 않았다면 반복 
    while bridgeInTrucks or truck_weights :
        currentTime += 1 
        
        # 다리를 지난 녀석을 체크해 줘야 함 
        if bridgeInTrucks :
            enterTime = bridgeInTrucks[0][0]
            checkTime = currentTime - enterTime
            
            if checkTime >= bridge_length :
                enterTime, truckWeight = bridgeInTrucks.popleft()
                bridgeInTrucksWeight -= truckWeight
    
        if truck_weights :
            # 1초에 한 대만 들어갈 수 있음 
            currentTruckWeight = truck_weights[0]
            if bridgeInTrucksWeight + currentTruckWeight <= weight :
                truck_weights.popleft()
                bridgeInTrucksWeight += currentTruckWeight
                bridgeInTrucks.append((currentTime, currentTruckWeight))
    
    return currentTime

