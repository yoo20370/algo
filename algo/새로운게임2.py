# N * N 체스판
# 사용하는 말의 개수 K개 - 1 ~ K번가지 번호 매겨져 있음, 이동방향 정해져 있음 (상하좌우로 이동 가능 )
# 하나의 말 위에 다른 말을 올릴 수 있다.
# 체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠 
# 한 턴은 1 ~ K번 말을 순서대로 이동시키는 것 

# 말의 이동방향에 있는 칸에 따라서 말의 이동이 다르다.
# 종료조건 -> 말이 4개이상 쌓이는 순간 게임 종료

# A번 말이 이동하려는 칸이
## 흰색 -> 그 칸으로 이동, 이동하려는 칸에 말이 이미 있는 경우 가장 위에 A번 말을 올려놓는다. ( A번 말 위에 있으면 같이 이동 )

## 빨간색 -> A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다. 이미 있는 경우 있는 말 위에 리버스하여 올린다. 

## 파란색 -> A번의 말의 이동방향을 반대로 하고 한 칸 이동, 방향을 반대로 바꾼 후 이동하려는 칸이 파란색인 경우 이동하지 않고 가만히 있는다.
## 체스판을 벗어나는 경우에는 파란색과 같은 경우이다. 

#### 입력 
# 체스판 크기 N, 말의 개수 K 
# 두 번째부터 체스판 정보 0 흰색, 1 빨간색, 2 파란색 
# N개 체스판 정보 이후 말의 정보가 주어진다.
# 3가지 정보, 행, 열, 이동방향 (행과 열은 1부터 시작, 이동방향은 1, 2, 3, 4 -> 동, 서, 북, 남)

################################################################################

import sys 

def find_index(list_a , target) :
    for curr_index in range(len(list_a)) :
        if list_a[curr_index] == target :
            return curr_index
    return -1

def new_game() :
    N, K = map(int, sys.stdin.readline().split())

    # 체스판 저장 
    pan = []
    for _ in range(N):
        pan.append(tuple(map(int, sys.stdin.readline().split())))


    # K개의 말 정보 저장 -> 순회해야하기 때문  
    horse_info_list = []

    horse_pan = [[[] for _ in range(N)] for _ in range(N)]

    for number in range(K) :
        row, col, distance = list(map(int, sys.stdin.readline().split()))
        horse_info_list.append([row-1, col-1, distance])    
        horse_pan[row-1][col-1].append(number)

    # for i in range(N) :
    #     for j in range(N) :
    #         print(horse_pan[i][j], end=" ")
    #     print()
    # print()
    
    # 방향정보
    # 동,서,북,남
    distance = {
        1 : (0,1),
        2 : (0,-1),
        3 : (-1,0),
        4 : (1,0)
    }

    reverse_distance = [0,2,1,4,3]

    # 어떻게 구현할 것인가요 ?? 
    # 3차원 배열에 말 위치 정보를 저장합니다. 
    # 특정 말이 이동하면 리스트 슬라이싱을 통해 이동시킬 리스트와 해당 위치에 있을 리스트를 구분하고 이동시킬 리스트에 대해서 이동 처리를 수행합니다. 
    turn = 1 
    while turn <= 1000 :
            
            index = 0 
            while index < len(horse_info_list) :
                curr_row, curr_col, curr_distance = horse_info_list[index]

                move_row, move_col = distance[curr_distance]

                next_row = curr_row + move_row
                next_col = curr_col + move_col

                # 파란색인 경우 
                if next_row == -1 or next_row == N or next_col == -1 or next_col == N or pan[next_row][next_col] == 2 :
                    curr_distance = reverse_distance[curr_distance]
                    horse_info_list[index][2] = curr_distance

                    move_row, move_col = distance[curr_distance]

                    next_row = curr_row + move_row
                    next_col = curr_col + move_col

                    # 반대편도 파란색이면 움직이지 않고 가만히 있는다.
                    if next_row == -1 or next_row == N or next_col == -1 or next_col == N or pan[next_row][next_col] == 2 :
                        index += 1
                        continue
                    
                    # 다시 처음부터 흰색인지 빨간색인지 확인하도록 하자
                    index -= 1

                elif pan[next_row][next_col] == 0 :
                    
                    # 원래 위치에서 리스트의 현재 말의 번호의 인덱스 추출 
                    f_index = find_index(horse_pan[curr_row][curr_col], index) 

                    # 이동할 리스트 추출
                    move_list = horse_pan[curr_row][curr_col][f_index:]

                    # 기존 위치 갱신 
                    horse_pan[curr_row][curr_col] = horse_pan[curr_row][curr_col][:f_index]

                    # 새로 이동할 위치의 리스트 갱신 
                    horse_pan[next_row][next_col] = horse_pan[next_row][next_col] + move_list

                    # 말의 현재 위치 정보 갱신 
                    horse_info_list[index][0] = next_row
                    horse_info_list[index][1] = next_col

                    for up_index in move_list :
                        horse_info_list[up_index][0] = next_row
                        horse_info_list[up_index][1] = next_col

                elif pan[next_row][next_col] == 1 :
                    
                    # 원래 위치에서 리스트의 현재 말의 번호의 인덱스 추출 
                    f_index = find_index(horse_pan[curr_row][curr_col], index) 

                    # 이동할 리스트 추출
                    move_list = horse_pan[curr_row][curr_col][f_index:]

                    # 거꾸로 변경
                    move_list.reverse()

                    # 기존 위치 갱신 
                    horse_pan[curr_row][curr_col] = horse_pan[curr_row][curr_col][:f_index]

                    # 새로 이동할 위치의 리스트 갱신 
                    horse_pan[next_row][next_col] = horse_pan[next_row][next_col] + move_list
                    
                    # 말의 현재 위치 정보 갱신 
                    horse_info_list[index][0] = next_row
                    horse_info_list[index][1] = next_col

                    for up_index in move_list :
                        horse_info_list[up_index][0] = next_row
                        horse_info_list[up_index][1] = next_col



                index += 1
                if len(horse_pan[next_row][next_col]) >= 4 :
                    return turn
                
            turn += 1 
    
    return -1

print(new_game())




