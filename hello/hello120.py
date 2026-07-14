# 정확한 순위 

import sys
from collections import deque

# 특정 번호의 학생은 탐색을 통해서 나머지 모든 원소로 이동할 수 있으면 순위를 알 수 있음
# 이긴 경우, 진 경우가 모두 있다면 혹은 다른 선수들의 결과로 추측할 수 있으면 순위가 결정될 수 있음 

def bfs(graph, start) :

    queue = deque([start])

    visited = set()

    while queue :
        current = queue.popleft()

        if current in visited :
            continue

        visited.add(current)

        for adjacent in graph[current] :
            if adjacent not in visited :
                queue.append(adjacent)

    return visited 


def solution() :
    studentCount, scoreCompareCount = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(studentCount + 1)]
    reverseGraph = [[] for _ in range(studentCount + 1)]

    for _ in range(scoreCompareCount) :
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        reverseGraph[end].append(start)

    count = 0
    for current in range(1, studentCount + 1) :

        resultSet1 = bfs(graph, current)
        resultSet2 = bfs(reverseGraph, current)

        result = resultSet1 | resultSet2
        if len(result) == studentCount :
            count += 1

    return count

result = solution()
print(result)
