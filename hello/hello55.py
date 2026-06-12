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

def dfsStack(graph, startNode) :

    stack = []

    visited = []

    stack.append(startNode)

    while stack : 
        currentNode = stack.pop()

        if currentNode in visited :
            continue 
        
        visited.append(currentNode)

        for adjacentNode in sorted(graph[currentNode], reverse=True) :
            if adjacentNode not in visited :
                stack.append(adjacentNode)

    return visited


def solution() :
    startNode = 1
    print(dfsStack(graph, startNode))
solution()