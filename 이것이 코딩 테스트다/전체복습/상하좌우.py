import sys

N = int(sys.stdin.readline().rstrip())

y = 1
x = 1

commands = sys.stdin.readline().split()

# L, R, U, D
listA = ["L", "R", "U", "D"]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# for command in commands :
#     idx = listA.index(command)

#     dx = x + xArr[idx]
#     dy = y + yArr[idx]
#     if command == "L" :
#         if dx == 0 :
#             continue
#         x = dx
#     elif command == "R" :
#         if dx == N :
#             continue
#         x = dx

#     elif command == "U" :
#         if dy == 0 :
#             continue 

#         y = dy
#     elif command == "D" :
#         if dy == N :
#             continue 
#         y = dy

# print(y, x)

for command in commands :

    for i in range(len(listA)) :
        if command == listA[i] :
            nx = x + dx[i]
            ny = y + dy[i]

    if nx > 0 and ny > 0 and nx < N + 1 and ny < N + 1 :
        x = nx 
        y = ny 

print(y, x)

    