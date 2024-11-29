# import sys

# N = int(sys.stdin.readline().rstrip())

# commands = sys.stdin.readline().split()

# x = 1
# y = 1
# for command in commands :  
#     if command == "L" and x - 1 != 0 :
#         x -= 1 
#     elif command == "R" and x + 1 != N + 1:
#         x += 1

#     elif command == "U" and y - 1 != 0 :
#         y -= 1
    
#     elif command == "D" and y + 1 != N + 1 :
#         y += 1
    
# print(y, x)


import sys

N = int(sys.stdin.readline().rstrip())

commands = sys.stdin.readline().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

movement = ["L", "R", "U", "D"]

x = 1
y = 1
for command in commands :
    for idx in range(len(movement)) :
        if command == movement[idx] :
            nx = x + dx[idx]
            ny = y + dy[idx]
    
    if nx > 0 and nx < N + 1 and ny > 0 and ny < N + 1 :
        x = nx 
        y = ny
print(x, y)


