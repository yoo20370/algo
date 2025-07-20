# 최대값과 최소값을 관리하는 이중 우선순위 큐라.....
# 두 개의 힙을 유지 ?? 
import heapq

def change_heap_type(heap) :
    
    temp = []
    temp = [-x for x in heap]
    heapq.heapify(temp)
    
    return temp
    
def solution(operations):
    
    heap = []
    check_heap_type = "min"
    
    # 어디서 런타임이 터질 수 있나 ?
    # 빈 큐에 데이터를 삭제하라고 할 떄 터질 수 있음 
    # 
    for string  in operations :
        command, value = string.split()
        
        if command == "I" :
            if check_heap_type == "min" :
                heapq.heappush(heap, int(value))
            else : 
                heapq.heappush(heap, -int(value))
        elif command == "D" and value == "1" and heap :
            # 최소힙이면 최대힙으로 만들어준다음에 반환해야함 
            if check_heap_type == "min" :
                heap = change_heap_type(heap)
                check_heap_type = "max"
                
            # 최대힙으로 만들어두고 반환하기 때문     
            heapq.heappop(heap)
            
        elif command == "D" and value == "-1" and heap:
            if check_heap_type == "max" :
                heap = change_heap_type(heap)
                check_heap_type = "min"
                
            # 최소힙으로 만들어두고 반환 
            heapq.heappop(heap)
                           
    if len(heap) >= 2 :
        # 최소힙이면 최소값이 출력, 최대힙이면 -최대값이 출력
        value1 = heapq.heappop(heap)
        
        heap = change_heap_type(heap)
        # 최소힙이면 -최대값, 최대힙이면 최소값 출력 
        value2 = heapq.heappop(heap)
        
        if check_heap_type == "min" :
            return [-value2, value1]
        else :
            return [-value1, value2]
    elif len(heap) == 1 :
        value = heapq.heappop(heap)
        
        if check_heap_type == "min" :
            return [value, value]
        else :
            return [-value, -value]
    else :
        return [0,0]
    
    
    return answer