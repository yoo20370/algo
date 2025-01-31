import sys

row, col = map(int, sys.stdin.readline().split())

curr_row, curr_col, curr_dis= map(int, sys.stdin.readline().split())

graph = list()
for i in range(row) :
    graph.append(list(map(int, sys.stdin.readline().split())))

# 북, 동, 남, 서
distance = [0, 1, 2, 3]

left_dis = [3, 0, 1, 2]

move_forward = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visit_cnt = 1
graph[curr_row][curr_col] = -1

rotation_cnt = 0
while True :
    # 왼쪽 방향으로 회전을 한다.
    curr_dis = left_dis[curr_dis]

    # 앞으로 이동하는 것이 가능한지 확인한다.
    forward_row, forward_col = move_forward[curr_dis]

    d_row = forward_row + curr_row
    d_col = forward_col + curr_col
    # 가능하다면 앞으로 이동한다.
    if graph[d_row][d_col] == 0 :
        visit_cnt += 1
        curr_row = d_row
        curr_col = d_col

        # 바다와 구분하기 위해서 -1로 기록 
        graph[d_row][d_col] = -1 

        # 회전수 초기화
        rotation_cnt = 0
    else :
        rotation_cnt += 1

        # 4번다 회전한 경우 
        if rotation_cnt == 4 :
            back_row, back_col = move_forward[curr_dis]

            d_row = -back_row + curr_row
            d_col = -back_col + curr_col

            # 뒤가 바다인 경우 탈출 
            if graph[d_row][d_col] == 1 :
                break
            else :
                # 뒤로 이동
                curr_row = d_row
                curr_col = d_col

                # 회전 수 초기화 
                rotation_cnt = 0

print(visit_cnt)
