
pan = list()
for i in range(19) :
    pan.append(list(map(int, input().split())))
    
N = int(input())

inputList = list()
for i in range(N) :
    x, y = map(int, input().split()) 
    inputList.append((x-1, y-1))

while inputList :
    x, y = inputList.pop()
    
    for i in range(19) :
        pan[x][i] = int(not(bool(pan[x][i])))
        pan[i][y] = int(not(bool(pan[i][y])))

for i in range(19) :
    for j in range(19) :
        print(pan[i][j], end=" ")
    print()