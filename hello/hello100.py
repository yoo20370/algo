# 2차 시도

# 내가 생각하지 못한 예외는 모든 도시를 방문해야 하므로 순차적으로 접근하는 경우로 모든 도시를 방문할 수 없는 경우 
# 다시 되돌아와서 다른 경로를 탐색해야 햔다는 것 
# 즉, 백트래킹이 필요해보임 
# dfs를 통해서 백트래킹을 해야 할 듯


import copy 

result = []
isAvailable = True

def dfs(begin, routeDict, resultList, visitedCityCount) : 
    
    global result 
    global isAvailable
    # 접근 했을 때 방문할 곳이 없으면 
    for destination in routeDict[begin] :
        copyResultList = copy.copy(resultList)
        # 방문 가능 
        if routeDict[begin][destination] > 0 :
            routeDict[begin][destination] -= 1
            copyResultList.append(destination)
            dfs(destination, routeDict, copyResultList, visitedCityCount)
            routeDict[begin][destination] += 1
    
    if len(resultList) == visitedCityCount and isAvailable:
        result = resultList
        isAvailable = False

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
    
    dfs('ICN', routeDict, ['ICN'], visitedCityCount)
    
    return result