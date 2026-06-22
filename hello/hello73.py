# 결국 1번 노드에서의 최단 거리를 구한 뒤, 
# 최대값을 구하고, 그 최대값에 해당하는 노드가 몇 개인지 선택하면 될 것 같음 

# 하나의 노드에서 다른 노드로 가는 건, 다익스트라 알고리즘이 있음 
import heapq

INF = int(1e9)

def solution(n, edge):
    
    edgeInfo = [[] for _ in range(n + 1)]
    
    
    for start, end in edge :
        # 양방향이기 때문 
        edgeInfo[start].append(end)
        edgeInfo[end].append(start)
    
    
    minDistanceList = [INF] * (n + 1)
    
    priorityQueue = []
    
    # [최단거리, 노드 번호]
    heapq.heappush(priorityQueue, [0, 1])
    minDistanceList[1] = 0
    
    while priorityQueue :
        currentCost, currentNode = heapq.heappop(priorityQueue) 
        
        # 이미 방문한 경우는 더 작을 것임
        if minDistanceList[0] < currentCost :
            continue
        
        for adjacentNode in edgeInfo[currentNode] :
            totalCost = currentCost + 1
            
            if minDistanceList[adjacentNode] > totalCost :
                minDistanceList[adjacentNode] = totalCost
                heapq.heappush(priorityQueue, [totalCost, adjacentNode])
    
    maxValue = 0
    for index in range(1, n + 1) :
        if minDistanceList[index] != INF and minDistanceList[index] > maxValue :
            maxValue = minDistanceList[index]

    answer = 0    
    for index in range(1, n + 1) :
        if maxValue == minDistanceList[index] :
            answer += 1
    
    return answer