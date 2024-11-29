# 왕실의 나이트 
import sys 

dx = [2, 2, -2, -2, 1, 1, -1 - 1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
cnt = 0

location = sys.stdin.readline().rstrip()

x = int(ord(location[0]) - 96)
y = int(location[1])

for i in range(len(dx)) :
    nx = x + dx[i]
    ny = x + dy[i]

    if nx > 0 and nx < 9 and ny > 0 and ny < 9 :
        cnt += 1

print(cnt)