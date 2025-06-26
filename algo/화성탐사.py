# 에너지를 효율적을 사용하고자 
## 화성 탐사 기계가 출발 지점에서 목표 지점까지 이동할 때 항상 최적의 경로를 찾도로 개발 

## N * N 크기의 2차원 공간 
## 각각의 칸을 지나기 위한 비용이 존재 
## 가장 왼쪽 위칸은 0,0 에서
## 가장 오른쪽 아래 n-1, n-1으로의 최소 비용을 출력하는 프로그램을 작성하여라  

############## 
# bfs로 풀어볼까 ?? 
# 단, 방문처리의 경우, 현재 위치의 최소값이 기록된 최소값보다 작다면 또 진행하는거지 
# 0,0에서 4방면으로 방문을 한다. 만약, 현재 위치에서 그 위치로 이동했을 때의 비용의 합이, 기록된 값보다 작다면 다시 탐색 실행 이렇게 되면 만약에 불필요한 연산이 무수히 많아질 수도 있네 ?? 
# 그럼 다익스트라로 푸는 것과 별 다를 것이 없을 것 같다. 

import sys, heapq

INF = int(1e9)

def mars_exploration() :

    size = int(sys.stdin.readline().rstrip())

    graph = [] 
    for _ in range(size) :
        graph.append(list(map(int, sys.stdin.readline().split())))

    # 최단 거리를 기록할 위치 
    distance = [[INF] * size for _ in range(size)]

    priority_queue = []
    heapq.heappush(priority_queue, (graph[0][0], 0, 0 ))
    distance[0][0] = graph[0][0]

    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while priority_queue :
        curr_cost, curr_row, curr_col = heapq.heappop(priority_queue)

        if distance[curr_row][curr_col] < curr_cost : 
            continue
        
        for move_row, move_col in direction :

            next_row = curr_row + move_row 
            next_col = curr_col + move_col 

            
            if next_row >= 0 and next_row < size and next_col >= 0 and next_col < size :
                temp_cost = curr_cost + graph[next_row][next_col]
                if distance[next_row][next_col] > temp_cost :
                    distance[next_row][next_col] = temp_cost
                    heapq.heappush(priority_queue, (temp_cost, next_row, next_col))
                

    print(distance[size-1][size-1])

def solution() :
    repeat_count = int(sys.stdin.readline().rstrip())

    for _ in range(repeat_count) :
        mars_exploration()

solution()

# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 20
# 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 19
# 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
# 36