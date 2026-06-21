from collections import deque

def solution(maps):
    direction = [(0,1), (0,-1), (1,0),(-1,0)]
    
    row = len(maps)
    col = len(maps[0])
    
    queue = deque()
    queue.append((0,0))
    
    while queue :
        curr_row, curr_col = queue.popleft()
    
        for move_row, move_col in direction :
            next_row = move_row + curr_row 
            next_col = move_col + curr_col
            
            if next_row >= 0 and next_row < row and next_col >= 0 and next_col < col :
                if maps[next_row][next_col] == 1:
                    queue.append((next_row, next_col))
                    maps[next_row][next_col] = maps[curr_row][curr_col] + 1
    
    result = -1 
    if maps[row-1][col-1] != 1 : 
        result = maps[row-1][col-1]
        
    return result