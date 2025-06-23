# 뱀이 기어다니는데 사과를 먹으면 뱀 길이가 늘어남
# 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝남 

# N * N 정사각 보드 위에서 진행 
# 몇몇 칸에는 사과가 놓여져 있다.
# 보드의 상하좌우 끝에는 벽이 존재 
# 맨위 맨 좌측에서(1행 1열) 시작하고 뱀의 길이는 1 

## 뱀은 처음에 오른쪽을 향한다. -> 방향이 있다.

# 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
# 만약 이동한 칸에 사과가 있다면 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다. 
# 만약 이동한 칸에 사과가 없다면 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

# deque를 사용해서 앞 뒤로 위치값을 넣었다가 빼야겠다.
# 중앙값은 변하지 않고 맨 앞과 맨 뒤만 바뀐다. 

# 0 0 -1 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

# (0,0) -> (0,1) -> (0,1), (0,2)

# 그러면 꼬리부터 넣어서 처리하는게 좋나 ?? 

import sys 
from collections import deque

def solution() :
    board_size = int(sys.stdin.readline().rstrip())

    K = int(sys.stdin.readline().rstrip())

    board_map = [[0] * board_size for _ in range(board_size)]

    for _ in range(K) :
        row, col = map(int, sys.stdin.readline().split())

        # -1은 사과 
        board_map[row-1][col-1] = -1
    
    # 자자 생각을 잘 해보자 
    # 우선 deque에 0,0을 넣어준다.
    # 사과를 만나는게 아니라면 deque에 새로운 위치값을 추가하고, deque에서 pop을 수행한다. 
    # 사과를 만나는거라면 deque에 새로운 위치값만 추가한다. 
    # 그리고 새로운 위치값이 벽이거나 deque에 존재하는 위치 중 하나라면 게임을 종료시킨다. 
    # 몇 초에 끝나는지 확인해라 해당 초는 0에서 시작하고 이동 명령을 수행하면서 1 씩 증가시킨다.

    # 동서남북 
    distance = {
        0 : (0, 1),
        1 : (0, -1),
        2 : (1, 0),
        3 : (-1, 0)
    }

    # 동서남북
    turn_left = [3, 2, 0, 1]
    turn_right = [2, 3, 1, 0]
 
    queue = deque()
    queue.append((0, 0))

    L = int(sys.stdin.readline().rstrip())

    info = []
    for _ in range(L) :
        info.append(sys.stdin.readline().split())

    info_index = 0
    curr_distance = 0 
    total_time = 0
    while True :

        move_row, move_col = distance[curr_distance] 

        # 뱀 머리 위치 
        curr_row, curr_col = queue[-1]

        next_row = curr_row + move_row
        next_col = curr_col + move_col

        # 게임 종료
        if next_row < 0 or next_row >= board_size or next_col < 0 or next_col >= board_size :
            # print("벽과 추돌")
            # print("어디?",next_row, next_col, curr_distance)
            return total_time + 1
        
        if (next_row, next_col) in queue:
            
            # print("뱀과 추돌")
            # print("어디?",next_row, next_col)
            return total_time + 1
        
        total_time += 1
        queue.append((next_row, next_col))
        # 길이가 증가하여 queue에서 좌표를 제거할 필요가 없음 
        if board_map[next_row][next_col] == - 1:
            board_map[next_row][next_col] = 0
        else :
            # 꼬리부분을 제거해야함 
            queue.popleft()

        if info_index < len(info) and int(info[info_index][0]) == total_time :
            if info[info_index][1] == "D" :
                curr_distance = turn_right[curr_distance]
            else : 
                curr_distance = turn_left[curr_distance]
            info_index += 1
            
    
    

print(solution())
# 0 1 2 3 4 5 6 7 8 9
# 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0 0 0 3
# 0 0 0 0 0 0 0 0 0 0 4
# 0 0 0 0 0 0 0 0 0 0 5
# 0 0 0 0 0 0 0 0 0 0 6
# 0 0 0 0 0 0 0 0 0 0 7
# 0 0 0 0 0 0 0 0 0 0 8
# 0 0 0 0 0 0 0 0 0 0 9
