# 하나의 우선순위 큐를 유지하고, 명령어가 변경될 때마다 우선순위 큐를 순회하여 최대힙, 최소 힙으로 만드는 방법
# 시간복잡도가 매우 커, 재시간에 못 풀 가능성이 큼 

# 힙을 두 개 활용하는 방법
# 최대힙, 최소힙을 두 개 유지하자 
# 그리고 최대힙이 pop한 List, 최소힙이 pop한 List를 유지해서 
# 실제 힙이 pop했을 때 동일한 값이 다른 힙에서 나온 적이 있다면 이를 무시하고 다시 pop한다.
# 힙의 길이를 변수로 관리하여, 힙에서 pop할 수 있는지 여부를 판단하여, 길이가 0이라면 pop 명령어 무시하게 한다.

import heapq

def solution(operations):
    
    maxHeap = []
    minHeap = []
    
    maxHeapPopList = {}
    minHeapPopList = {}
    
    heapLength = 0
    
    for operation in operations :
        command, number = operation.split()
        
        if command == "I" :
            number = int(number)
            
            heapq.heappush(maxHeap, -number)
            heapq.heappush(minHeap, number)
            
            heapLength += 1
        
        else :
            if heapLength < 1 :
                continue 
                
            heapLength -= 1
            
            if number == "1" :
                popValue = None 
                while maxHeap :
                    popValue = - heapq.heappop(maxHeap)
                    
                    if minHeapPopList.get(popValue) and minHeapPopList.get(popValue) >= 1 :
                        minHeapPopList[popValue] -= 1
                        continue
                        
                    break
                    
                if popValue is not None :
                    if maxHeapPopList.get(popValue) :
                        maxHeapPopList[popValue] += 1
                    else :
                        maxHeapPopList[popValue] = 1
            else :
                popValue = None 
                while minHeap :
                    popValue = heapq.heappop(minHeap)
                    
                    if maxHeapPopList.get(popValue) and maxHeapPopList.get(popValue) >= 1 :
                        maxHeapPopList[popValue] -= 1
                        continue
                        
                    break
                        
                if popValue is not None :
                    if minHeapPopList.get(popValue) :
                        minHeapPopList[popValue] += 1
                    else :
                        minHeapPopList[popValue] = 1

    if heapLength < 1 :
        return [0, 0]
    else :
        
        maxValue = None
        while True :
            maxValue = - heapq.heappop(maxHeap)
            
            if minHeapPopList.get(maxValue) and minHeapPopList.get(maxValue) >= 1 :
                minHeapPopList[maxValue] -= 1
                continue
        
            break
        
        minValue = None
        while True :
            minValue = heapq.heappop(minHeap)
            
            if maxHeapPopList.get(minValue) and maxHeapPopList.get(minValue) >= 1 :
                maxHeapPopList[minValue] -= 1
                continue
            break
        
        return [maxValue, minValue]
                
        