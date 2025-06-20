########## 문제점 너무 느림 이유를 찾아보자 

# 파란 구슬과 빨간 구슬을 하나씩 넣은 다음, 빨간 구슬을 통해 빼내는 게임 

# 보드의 세로 크기는 N 가로 크기는 M, 편의상 1 X 1 크기의 칸으로 나누어져 있다.
# 보드에는 구멍이 하나 존재
# 빨간 구슬만 들어가고 파란 구슬이 들어가면 안 된다. 

# 동작은 왼쪽, 오른쪽, 위, 아래로 기울이기만 가능 -> 한 쪽으로 기울이면 구슬은 벽이나 다른 구슬을 마주할 때까지 이동해야 함 
# 구슬은 동시에 움직인다. 구슬은 같은 칸에 있을 수 없다.

#####################################################

# BFS로 풀어야겠다. 라고 했습니다. -> 무엇을 큐에 넣어야하냐 이게 핵심이다.
# 두 구슬의 위치가 동일한 것에 대해서는 다시 방문하지 않도록 해야 한다. 
# 4차원 배열을 통해서 이를 기록한다.
# 그리고 큐에는 파란 구슬 위치와 빨간 구슬 위치 그리고 몇 번째 턴인지를 기록한다. -> 몇 번째 턴인지 반환해야 하기 때문 
# 총 10번 턴만 가능하므로, 시간복잡도가 높은 자료구조를 사용해도 된다. 
# 구슬이 겹치는 경우를 위해서, 이동하는 횟수를 구해서 이동하는 횟수가 더 많은 것이 뒤에 있으므로 이를 변경해준다. -> 둘이 겹칠 때만 

# 이동 시킨 위치를 기준으로 기록하자. -> 그 이후에 행위는 동일할 것이기 때문 

import sys 
from collections import deque

def move_beed(board, curr_row, curr_col, move_row, move_col) :

    # 다음 위치가 벽이 아니라면 이동
    # 현재 위치가 구멍이라면 break 후 반환 
    
    move_count = 0
    while True :
    
        if board[curr_row][curr_col] == "O" :
            return curr_row, curr_col, move_count
        
        next_row = curr_row + move_row 
        next_col = curr_col + move_col

        if board[next_row][next_col] == "#" :
            return curr_row, curr_col, move_count
        
        move_count += 1 

        curr_row = next_row
        curr_col = next_col

def beed_game() :

    row, col = map(int, sys.stdin.readline().split())

    # 방문처리용 
    visited = set()
    
    # 구슬판 만들기
    board = []
    for _ in range(row) :
        board.append(sys.stdin.readline().rstrip())
    
    # 파란 구슬과 빨간 구슬 위치 찾기 
    blue_row, blue_col, red_row, red_col = -1, -1, -1, -1
    for i in range(row) :
        for j in range(col) :
            if board[i][j] == "R" :
                red_row, red_col = i, j 
            elif board[i][j] == "B" :
                blue_row, blue_col = i, j

    queue = deque()
    queue.append([blue_row, blue_col, red_row, red_col, 1])
    visited.add((blue_row, blue_col, red_row, red_col)) 

    # 동서남북 
    distance = {
        0 : (0, 1),
        1 : (0, -1),
        2 : (1, 0),
        3 : (-1, 0)
    }
    
    # 첫 번째 턴부터 10번째까지 수행할 예정 
    while queue :
        blue_row, blue_col, red_row, red_col, curr_turn = queue.popleft()

        if curr_turn > 10 :
            break

        for i in range(4) :
            # 어떻게 설계할건데 ??
            # 둘 다, 구슬을 이동시킨다.
            # 만약 반환된 위치가 0 구슬이라면 탈출한 것 이때, 파란 구슬도 탈출했는지 확인한다.
            # 만약 두 구슬의 위치가 겹친다면, move_count 값이 더 큰 쪽을 이동한 위치 하나를 뒤로 이동시킨다.
            # 만약 방문한 적이 없는 위치라면 queue에 삽입한다. 이때 turn_count 값을 1 증가시킨다.

            move_row, move_col = distance[i]

            r_row, r_col, red_move_count = move_beed(board, red_row, red_col, move_row, move_col)
            b_row, b_col, blue_move_count = move_beed(board, blue_row, blue_col, move_row, move_col)
            # 파란 구슬도 빠진 경우 
            if board[b_row][b_col] == "O" :
                continue

            # 구슬이 구멍으로 빠졌을 때, 
            if board[r_row][r_col] == "O" :
                return curr_turn

            if r_row == b_row and r_col == b_col :
                if red_move_count > blue_move_count :
                    r_row -= move_row
                    r_col -= move_col
                else :
                    b_row -= move_row
                    b_col -= move_col

            if (b_row, b_col, r_row, r_col) not in visited :
                queue.append([b_row, b_col, r_row, r_col, curr_turn + 1])
    return -1

print(beed_game())

