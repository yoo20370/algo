# N, M = map(int, input().split())

# pan = []
# for i in range(N) :
#     pan.append(input())

# def func(startRow, startColumn, pan) :
#     cnt = 0 
#     k = 1
#     for i in range(startRow, startRow + 8) :
#         for j in range(startColumn, startColumn + 7, k) :
        
#             if pan[i][j] == 'B' :
#                 if pan[i][j + 1] == 'B' :
#                     # pan[i][j + 1] ='W'
#                     cnt += 1
#             else :
#                 if pan[i][j + 1] == 'W' :
#                     # pan[i][j + 1] ='B'
#                     cnt += 1
#     return cnt

# print(func(0,0,pan))

N, M = map(int, input().split())

pan = []

for i in range(N) :
    pan.append(input())

result = list()

# 시작점을 위한 
for i in range(0, N - 7) :
    for j in range(0, M - 7) :
        draw1 = 0
        draw2 = 0

        for a in range(i, i + 8) :
            for b in range(j, j + 8) :
                if (a + b) % 2 == 0 :
                    if pan[a][b] != 'W' :
                        draw1 += 1
                    if pan[a][b] != 'B' :
                        draw2 += 1
                else :
                    if pan[a][b] != 'B' :
                        draw1 += 1
                    if pan[a][b] != 'W' :
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)
print(min(result))

# def func(startRow, startColumn, pan) :
#     pan_copy = deepcopy(pan)
#     cnt = 0 
#     k = 1
#     for i in range(startRow, startRow + 7) :
#         for j in range(startColumn, startColumn + 7, k) :
#             if pan_copy[i][j] == 'B' :
#                 if pan_copy[i][j + 1] == 'B' :
#                     pan_copy[i][j + 1] ='W'
#                     cnt += 1
#             else :
#                 if pan_copy[i][j + 1] == 'W' :
#                     pan_copy[i][j + 1] ='B'
#                     cnt += 1
#     return cnt

# min = 999999999
# for i in range(0, N - 7) :
#     for j in range(0, M - 7):
#         cnt = func(i, j, pan)
#         if min > cnt :
#             min = cnt

# print(min)