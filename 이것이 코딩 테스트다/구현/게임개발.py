# import sys 

# N, M = map(int, sys.stdin.readline().split())
# X, Y, Look = map(int, sys.stdin.readline().split())
# pan = []

# # 북, 동, 남, 서 - 인덱스
# Looks = [0, 1, 2, 3]

# # 왼쪽으로 돌았을 때 - 인덱스
# left = [3, 0, 1, 2]

# # 뒤로 이동할 때 - 인덱스
# back = [2, 3, 0 ,1]

# # 좌표 
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]

# # 현재 위치 방문 


# for i in range(N) :
#     pan.append(list(map(int, sys.stdin.readline().split())))

# # 시작 위치 체크 
# cnt = 1
# pan[X][Y] = 1

# # Look은 회전 전 기준 
# dLook = Look
# while True :
#     nx = X + dx[dLook]
#     ny = Y + dy[dLook]

#     # 바라보는 방향 왼쪽으로 가보지 않은 경우 
#     if pan[nx][ny] != 1 :
#         pan[nx][ny] = 1
#         print(nx, ny)
        
#         # 회전 
#         Look = left[Look]
#         dLook = Look

#         # 이동 
#         X = nx
#         Y = ny 

#         cnt += 1
#     else :
#         # 한 바퀴 돈 경우
#         if left[dLook] == Look :
#             # 원래 방향으로 회전 
#             dLook = Look

#             # 뒤로 이동
#             X += dx[back[Look]] 
#             Y += dy[back[Look]]

#             # 뒤로 이동한 곳이 바다인 경우 탈출 
#             if pan[X][Y] == 1 :
#                 break
#         else :
#             # 왼쪽으로 회전 
#             dLook = left[dLook]

# print(cnt)        

import sys

N, M = map(int, sys.stdin.readline().split())

x, y, dis = map(int, sys.stdin.readline().split())

pan = list()

for _ in range(N) :
    pan.append(list(map(int, sys.stdin.readline().split())))

# 북, 동, 남, 서
distance = [0, 1, 2, 3]
left = [3, 0, 1, 2]
back = [2, 3, 0, 1]
dx_left = [0, -1, 0, 1]
dy_left = [-1, 0, 1, 0]

dx_back = [1, 0, -1, 0]
dy_back = [0, -1, 0, 1]


cnt = 1
pan[x][y] = 2

curr = dis 
while True :

    # 한 바퀴 돈 경우 
    if left[curr] == dis :
        # 처음 방향으로 회전 
        curr = left[curr]

        # 뒤쪽으로 이동 
        x = x + dx_back[curr]
        y = y + dx_back[curr]

        if pan[x][y] == 1 :
            break

    else :
        nx = x + dx_left[curr]
        ny = y + dy_left[curr]

        # 해당 방향으로 회전 
        curr = left[curr]

        # 이동 가능한 경우
        if pan[nx][ny] == 0 :
            # 이동 
            x = nx
            y = ny 

            dis = curr 

            pan[x][y] = 2
            cnt += 1

print(cnt)

