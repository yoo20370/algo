graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 순으로 나와야 함 

# 재귀함수 dfs 
def dfsRecursion(graph, currentNode, visited) :

    # 방문한 적이 있다면
    if currentNode in visited :
        return 
    
    visited.append(currentNode)
    
    for adjacentNode in graph[currentNode] :
        if adjacentNode not in visited :
            dfsRecursion(graph, adjacentNode, visited) 


def solution(graph) :

    # set으로 하는게 시간복잡도에 좋지만, 추가 메모리 공간 없이 visited만으로 하려고 list 사용 
    visited = []
    startNode = 1
    dfsRecursion(graph, startNode, visited)

    print(visited)

solution(graph)

