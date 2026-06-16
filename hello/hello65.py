# 더 맵게

# 모든 스코빌 지수를 K 이상으로 만들고 싶음 
# Leo는 스코빌 지수가 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식은 만든다. 

# 결국 그거네 힙에 모든 음식을 삽입 
# 힘의 최상위 노드가 K보다 작다면 가장 스코빌 지수가 낮은 음식 두가지를 꺼내서 섞은 음식 스코빌 지수를 만들고 
# 힙에 다시 삽입 

# 힙의 최상위 노드가 K보다 크거나 같다면 만족하므로 음식을 섞은 횟수를 반환하도록 하자 

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
import heapq

def solution(scoville, K):
    
    minHeap = []
    
    for food in scoville :
        heapq.heappush(minHeap, food)
    
    mixCount = 0
    while len(minHeap) >= 2 and minHeap[0] < K :
        firstFood = heapq.heappop(minHeap)
        secondFood = heapq.heappop(minHeap)

        newFood = firstFood + secondFood * 2 

        heapq.heappush(minHeap, newFood)
        mixCount += 1
        
    if minHeap[0] < K :
        return -1
    
    return mixCount
    
    