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