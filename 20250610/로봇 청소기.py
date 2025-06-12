import sys 

def robot_cleaner() :
    row, col = map(int, sys.stdin.readline().split())

    start_row, start_col, start_distance = map(int, sys.stdin.readline().split())

    room= []
    for _ in range(row) :
        room.append(list(map(int, sys.stdin.readline().split())))

    # 각각의 칸은 벽 또는 빈 칸으로 구성 
    # 청소기는 바라보는 방향이 있음, 동서남북, 
    # 방의 각 칸은 r,c로 나타낼 수 있다.
    # 가장 북쪽 줄의 가장 서쪽 칸의 좌표가 (0,0)
    # 가장 남쪽 줄의 가장 동쪽 칸의 좌표가 (-1, -1)

    # 어떻게 구현할까 ?? 

    # 북, 동, 남, 서 
    distance = [0, 1, 2, 3]
    turn_left = [3, 0, 1, 2]
    move_forward = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    total_count = 0
    # 처음 이동한 경우, 해당 구역이 청소되었는지 확인, 청소되어있지 않다면 청소를 수행한다.
    # 왼쪽으로 회전하고, 앞의 구역이 청소되지 않았다면 앞으로 이동한다.(전체 반복문으로 돌아간다.)
    # 회전의 경우 4번을 반복하고 한 바뀌 회전했음에도 모두 청소한 구역이라면, 뒤로 이동한다., 뒤로 이동할 수 없다면 전체 반복문을 회전한다. 
    # 뒤로 이동한 뒤 전체 반복문으로 돌아간다.

    curr_row = start_row
    curr_col = start_col
    curr_distance = start_distance
    while True :

        # 청소 수행
        if room[curr_row][curr_col] == 0 :
            room[curr_row][curr_col] = -1 
            total_count += 1
        
        # 왼쪽으로 회전하며 앞의 좌표가 청소 가능한 구역인지 확인 
        for _ in range(4) :
            # 회전
            curr_distance = turn_left[curr_distance]
            move_row, move_col = move_forward[curr_distance]

            next_row = curr_row + move_row
            next_col = curr_col + move_col
        
            if room[next_row][next_col] == 0 :
                curr_row = next_row
                curr_col = next_col
                break
            
        else :
            move_row, move_col = move_forward[curr_distance]

            back_row = curr_row - move_row
            back_col = curr_col - move_col

            if room[back_row][back_col] == 1 :
                return total_count
            
            curr_row = back_row
            curr_col = back_col







print(robot_cleaner())