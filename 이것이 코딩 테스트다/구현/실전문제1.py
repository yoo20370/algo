# 왕실의 나이트 
# import sys 

# dx = [2, 2, -2, -2, 1, 1, -1 - 1]
# dy = [1, -1, 1, -1, 2, -2, 2, -2]
# cnt = 0

# location = sys.stdin.readline().rstrip()

# x = int(ord(location[0]) - 96)
# y = int(location[1])

# for i in range(len(dx)) :
#     nx = x + dx[i]
#     ny = x + dy[i]

#     if nx > 0 and nx < 9 and ny > 0 and ny < 9 :
#         cnt += 1

# print(cnt)

# 현재 나이트 위치 입력 
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a')) + 1)

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인 ;
result = 0
for step in steps :
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
        result += 1

print(result)