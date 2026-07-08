# 1차 시도 실패 

# 방문은 여러 번 할 수 있어야 함 -> 방문 처리 필요 없음 
# 큐를 사용하자
# 큐에서 하나씩 뽑아서 처리하면 좋을 것 같음 

# 이 로직에서 모두 이용 못하는 경우가 뭐가 있을까 ? 
# 혹시 동일한 출발지, 목적지에 대해서는 무시해야 하는건가 ?
# 그러면 안 되는게 모든 항공권 사용해야 함.... 동일한 항공권이 있다면 그것도 쓸 수 있어야지 
from collections import deque 

def solution(tickets):
    
    routeDict = {}
    visited = set()
    
    for ticket in tickets :
        begin, destination = ticket 
        
        if routeDict.get(begin) is None :
            routeDict[begin] = [destination]
        
        else :
            routeDict[begin].append(destination)
            
        if routeDict.get(destination) is None :
            routeDict[destination] = []
    
    for begin in routeDict :
        sortedRoutes = sorted(routeDict[begin])
        routeDict[begin] = deque(sortedRoutes)
    
    resultList = []
    stack = ['ICN']
    
    while stack :
        currentBegin = stack.pop()
        
        destinationQueue = routeDict[currentBegin]
        
        # 큐가 비어있다면 건너뛴다. 
        # 더 이상 이동할 수 있는 곳이 없다는 의미 
        if not destinationQueue :
            resultList.append(currentBegin)
            break
        
        destination = destinationQueue.popleft()
        resultList.append(currentBegin)
        stack.append(destination)
    
    return resultList