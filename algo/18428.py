# 특정한 위치에 선생님, 학생, 장애물이 위치할 수 있다. 
# 몇 몇의 학생은 몰래 복도로 빠져 나옴
## 복도로 빠져나온 학생들은 선생님의 감시에 들키지 않는 것이 목표 
## 각 선생님은 상, 하, 좌, 우 방향으로 감시를 진행 
## 단 장애물이 위치한 경우, 선생님은 장애문 뒤편에 숨어 있는 학생들을 볼 수 없다. 
## 또한 선생님은 상하 좌우 4가지 방향에 대하여, 아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다.
## (행,열) 형태로 표현 
## 선생님이 존재하는 칸은 T, 학생이 존재하는 칸은 S 장애물이 존재하는 칸은 O로 표시 

#################################################################3

# 어떻게 풀 것인가 ?? 
# 항상 빈 칸의 개수는 3개 이상으로 주어진다. 
# 선생님 수는 5이하 전체 학생 수는 30이하의 자연수 

## 결국 또 조합을 이용해서 선생님과, 학생이 없는 위치에 대하여 3개의 장애물을 무작위로 설치하고, 
## 그 때마다 선생님에 대하여 상하좌우로 너비 우선 탐색 한 번 실행 이 때, 각 너비 우선 탐색은
## 딱 한 번만 실행하되 직선 방향으로 수행한다. 이 때, O를 만나거나 끝에 도달하면 끝난다. 
## 이 때 한 번이라도 만나는 적이 없다면 바로 YES 출력 후, 종료 그렇지 않으면 제거 

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

    # 쉽게 말하자면 선생님을 기준으로 상하좌우로 탐색을 수행할 것임 
    # queue에 들어가는 값은 상하좌우 한 칸 씩만 탐색 
    # diretion_queue의 경우는 한 방향으로 탐색을 수행하도록 할 것임 

    # row 상하, col 좌우
    direction = [(1,0), (-1,0), (0, 1), (0, -1)]

    ## 이걸 함수로 묶어야 편할 것 같은데 
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