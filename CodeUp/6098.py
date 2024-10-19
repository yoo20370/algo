
# pan = list()

# for i in range(10) :
#     pan.append(list(map(int, input().split())))

# x = 1
# y = 1
# while True :
#     if pan[x][y] == 2 or (x == 8 and y == 8):
#         pan[x][y] = 9
#         break
#     # 현재 위치 확정
#     pan[x][y] = 9
   
#     if pan[x][y+1] == 1 :
#         x += 1
#         continue
#     y += 1

# for i in range(10) :
#     for j in range(10) :
#         print(pan[i][j], end=" ")
#     print()

pan = list()

for i in range(10) :
    pan.append(list(map(int, input().split())))

x = 1
y = 1

while True :
    
    if pan[x][y] == 2 or (x == 8 and y == 8) :
        pan[x][y] = 9
        break
    pan[x][y] = 9
    if pan[x][y+1] == 1 :
        x += 1
    else :
        y += 1

for i in range(10) :
    for j in range(10) :
        print(pan[i][j], end=" ")
    print()



