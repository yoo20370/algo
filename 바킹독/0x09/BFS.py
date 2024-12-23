from collections import deque

def bfs(graph, start) -> None :
    row, column = start 

    route = [(0, 1), (0, -1), (1,0), (-1, 0)]

    queue = deque()
    queue.append((row, column))
    graph[row][column] 

    while queue :
        curr_row, curr_col = queue.popleft()

        for d_row, d_col in route :
            n_row = curr_row + d_row 
            n_col = curr_col + d_col 

            if n_row >= 0 and n_row < (len(graph) // graph[0]) and n_col >= 0 and n_col < len(graph[0]) and graph[n_row][n_col]:
                graph[n_row][n_col] = 1
                queue.append((n_row, n_col))
                


