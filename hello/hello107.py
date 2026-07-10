# 1 ~ N번 까지의 도시와 M개의 단방향 도로 존재 
# 모든 도로의 거리는 1
# 이때 특정 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중, 최단 거리가 정확히 K인 도시의 번호를 출력하는 프로그램 작성 

# 최단거리라는 키워드 때문에 다익스트라를 떠올렸지만, 이 문제는 bfs가 더 적합하다고 한다. 
import sys
from collections import deque

def solution() :

    cityCount, loadCount, k, beginCity = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(cityCount + 1)]
    for _ in range(loadCount) :
        begin, end = map(int, sys.stdin.readline().split())
        graph[begin].append(end)

    queue = deque()

    visited = set()
    visited.add(beginCity)

    # (현재 도시, 누적비용) 
    queue.append((beginCity, 0))

    while queue :
        currentCity, currentCost = queue.popleft()

        for adjacentCity in graph[currentCity] :
            if adjacentCity not in visited :
                queue.append([adjacentCity, currentCost + 1])
                visited.add(adjacentCity)
                if currentCost + 1 == k :
                    print(adjacentCity)

solution()