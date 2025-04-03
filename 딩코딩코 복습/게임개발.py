import sys 

max_row, max_col = map(int, sys.stdin.readline().split())

start_row, start_col, start_distance = map(int, sys.stdin.readline().split())

map_data = []

for _ in range(max_row) :
    map_data.append(list(map(int, sys.stdin.readline().split())))

def gameDev(max_row, max_col, start_row, start_col, start_distance, map_data) -> int :

    total_count = 0

    # 북, 동, 남, 서
    distance = [0, 1, 2, 3]
    turn_left = [3, 0, 1, 2] 
    forward_step = [(-1,0), (0,1), (1,0),(0,-1)]
    
    curr_row = start_row
    curr_col = start_col
    curr_dis = start_distance

    while True :
        # 1. 현재 위치를 청소했는지 체크한다. (0이면 청소하지 않은 것, -1이면 청소한 것)
        # 2. 회전한 후, 앞으로 이동 가능한지 확인한다. , 만약 이동이 가능하다면 이동하고 그렇지 않은 경우 회전한다.
        # 3. 한 바퀴 회전한 경우, 뒤로 이동한다. 이 때, 뒤가 바다라면 반복문을 탈출한다. 
        if map_data[curr_row][curr_col] == 0 :
            map_data[curr_row][curr_col] = -1
            total_count += 1 

    
        for _ in range(4) :
            # 회전
            curr_dis = turn_left[curr_dis]

            # 앞으로 이동
            row, col = forward_step[curr_dis]         
            now_row = curr_row + row
            now_col = curr_col + col

            # 밖으로 나가지도 않고, 청소하지 않은 경우 
            if now_row >= 0 and now_row < max_row and now_col >= 0 and now_col < max_col and map_data[now_row][now_col] == 0 :
                # 이동 후 처음으로 돌아가기 
                curr_row = now_row
                curr_col = now_col
                break
        else : 
            row, col = forward_step[curr_dis]

            # 뒤로 이동 
            now_row = curr_row - row
            now_col = curr_col - col

            if now_row >= 0 and now_row < max_row and now_col >= 0 and now_col < max_col and map_data[now_row][now_col] != 1 :
                curr_row = now_row
                curr_col = now_col
            else :
                break
            
    return total_count

print(gameDev(max_row, max_col, start_row, start_col, start_distance, map_data))

        



    
