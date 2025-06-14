import sys
from collections import deque
def virus() :
    computer_count = int(sys.stdin.readline().rstrip())
    edge_count = int(sys.stdin.readline().rstrip())

    graph = [[] for _ in range(computer_count + 1)]
    for _ in range(edge_count) :
        start, end = map(int, sys.stdin.readline().split())

        graph[start].append(end)
        if start not in graph[end] :
            graph[end].append(start)
    
    visited = set()

    start_computer = 1 
    queue = deque()
    queue.append(start_computer)

    infection_count = 0
    while queue :
        curr_computer = queue.popleft()
        if curr_computer not in visited :
            visited .add(curr_computer)
            infection_count += 1


        for near_computer in graph[curr_computer] :
            if near_computer not in visited :
                queue.append(near_computer)

    print(infection_count - 1)

virus()