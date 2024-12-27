import sys

row, col = map(int, sys.stdin.readline().split())

r, c, d = map(int, sys.stdin.readline().split())

# 북, 동, 남, 서 
distance = [0, 1, 2, 3]

# 왼쪽으로 회전할 때 distance
turn_left = [3, 0, 1, 2]

# 해당 방향에서 앞으로 가는 경우
forward = [(-1,0), (0,1), (1,0), (0, -1)]

home_map = []

total_cnt = 0

for _ in range(row) :
    home_map.append(list(map(int, sys.stdin.readline().split())))

while True :
    # 1. 현재 칸 청소
    if home_map[r][c] == 0 :
        home_map[r][c] = -1
        total_cnt += 1
    
    cnt = 0 
    while cnt != 4 :
        d = turn_left[d]

        d_r, d_c = forward[d]

        n_r = r + d_r
        n_c = c + d_c 

        # 현재 앞 블록이 청소가 안 된 경우 이동 
        if home_map[n_r][n_c] == 0 :
            r = n_r
            c = n_c
            break
        else :
            # 현재 앞 블록이 청소가 된 경우 반시계 방향으로 90도 회전 
            cnt += 1

    # 1번으로 이동
    if cnt == 4 :
        # 뒤로 이동
        d_r, d_c = forward[d]

        n_r = r - d_r
        n_c = c - d_c

        # 뒤로 갔는데 벽인 경우 멈춘다.
        if home_map[n_r][n_c] == 1 :
            break

        else :
            r = n_r
            c = n_c
    

print(total_cnt)