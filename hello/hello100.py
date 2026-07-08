# 2차 시도

# 내가 생각하지 못한 예외는 모든 도시를 방문해야 하므로 순차적으로 접근하는 경우로 모든 도시를 방문할 수 없는 경우 
# 다시 되돌아와서 다른 경로를 탐색해야 햔다는 것 
# 즉, 백트래킹이 필요해보임 
# dfs를 통해서 백트래킹을 해야 할 듯

def dfs(begin, routeDict, resultList, visitedCityCount) : 
    
    if len(resultList) == visitedCityCount:
        return True
    
    # 접근 했을 때 방문할 곳이 없으면 
    for destination in routeDict[begin] :

        # 방문 가능 
        if routeDict[begin][destination] > 0 :
            routeDict[begin][destination] -= 1
            resultList.append(destination)
            if dfs(destination, routeDict, resultList, visitedCityCount) :
                return True
            resultList.pop()
            routeDict[begin][destination] += 1
    
    return False

def solution(tickets):
    
    routeDict = {}
    visitedCityCount = len(tickets) + 1

    for ticket in tickets :
        begin, destination = ticket
        
        if routeDict.get(begin) is None :
            routeDict[begin] = {}
            routeDict[begin][destination] = 1
        else : 
            if routeDict[begin].get(destination) is None :
                routeDict[begin][destination] = 1
            else :
                routeDict[begin][destination] += 1
                
        if routeDict.get(destination) is None :
            routeDict[destination] = {}
    
    
    for begin in routeDict :
        destinationList = list(routeDict[begin].items())
        routeDict[begin] = dict(sorted(destinationList))
    
    resultList = ['ICN']
    dfs('ICN', routeDict, resultList , visitedCityCount)
    
    return resultList