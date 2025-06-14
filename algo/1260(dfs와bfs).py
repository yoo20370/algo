import sys
from collections import deque

def bfs(start, graph) :

    visited = set()
    queue = deque()
    queue.append(start)

    while queue :
        curr_node = queue.popleft()
        if curr_node not in visited :
            visited.add(curr_node)
            print(curr_node, end=" ")

        for near_node in sorted(graph[curr_node]) :
            if near_node not in visited :
                queue.append(near_node) 

def dfs(start, graph) :

    visited = set()
    stack = []
    stack.append(start)

    while stack :
        curr_node = stack.pop()
        if curr_node not in visited :
            visited.add(curr_node)
            print(curr_node, end=" ")

        for near_node in sorted(graph[curr_node], reverse=True) :
            if near_node not in visited :
                stack.append(near_node)

node_count, edge_count, start_node = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(node_count + 1)]

for _ in range(edge_count) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

dfs(start_node, graph)
print()
bfs(start_node, graph)