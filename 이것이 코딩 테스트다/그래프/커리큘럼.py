import sys, copy
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = [ [] for i in range(N+1) ]
cost = [0 for i in range(N+1)]
entryOrder = [0 for i in range(N+1)]

for num in range(1, N+1) :
    inputData = list(map(int, sys.stdin.readline().split()))
    cost[num] = inputData[0]

    for i in range(1, len(inputData) -1) :
        graph[inputData[i]].append(num)
        entryOrder[num] += 1

def func() :
    result = copy.deepcopy(cost)
    queue = deque()

    # 진입차수가 0인 경우 모두 넣는다. 
    for idx in range(1, N+1) :
        if entryOrder[idx] == 0 :
            queue.append(idx)

    while queue :
        startNode = queue.popleft()

        for endNode in graph[startNode] :
            result[endNode] = max(result[endNode], result[startNode] + cost[endNode])
            entryOrder[endNode] -= 1
            if entryOrder[endNode] == 0 :

                queue.append(endNode)
    return result
    
result = func()
for i in range(1, N+1) :
    print(result[i])

