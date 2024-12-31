import sys
from collections import deque

INF = int(1e9)

F, S, G, U, D = map(int, sys.stdin.readline().split()) 

floors = [INF] * (F+1)

queue = deque()
queue.append(S)
floors[S] = 0

while queue :
    curr = queue.popleft()

    if curr - D > 0 and floors[curr - D] == INF :
        floors[curr - D] = min(floors[curr - D], floors[curr] + 1)
        queue.append(curr - D)

    if curr + U < (F+1) and floors[curr + U] == INF :
        floors[curr + U] = min(floors[curr + U], floors[curr] + 1)
        queue.append(curr + U)

if floors[G] >= INF :
    print("use the stairs")
else :
    print(floors[G])


