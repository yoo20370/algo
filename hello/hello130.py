import sys, itertools 
from collections import deque

def solution() :

    N = int(sys.stdin.readline().rstrip())

    graph = []
    for _ in range(N) :
        graph.append(list(sys.stdin.readline().split()))

    student_position_list = []
    teacher_position_list = []
    empty_position_list = []
    
    for i in range(N) :
        for j in range(N) :
            if graph[i][j] == 'T' :
                teacher_position_list.append((i,j))
            elif graph[i][j] == 'X' :
                empty_position_list.append((i,j))
    

    for object_position_list in itertools.combinations(empty_position_list, 3) :
    
        if catch_student(graph, N, teacher_position_list, object_position_list) :
            return "YES"
    
    return "NO"

def catch_student(graph, N, teacher_position_list, object_position_list) :

    direction = [(1,0), (-1,0), (0, 1), (0, -1)]

    queue = deque(teacher_position_list)
    
    while queue :
        curr_row, curr_col = queue.popleft()
        for move_row, move_col in direction :

            next_row = curr_row + move_row 
            next_col = curr_col + move_col 

            while 0 <= next_row < N and 0 <= next_col < N :
                if (next_row, next_col) in object_position_list :
                    break
                if graph[next_row][next_col] == 'S' :
                    return False
                
                next_row += move_row
                next_col += move_col

    return True

print(solution())