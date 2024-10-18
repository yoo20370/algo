N = int(input())

badock = [[0] * 19 for _ in range(19)]

inputList = list()
for i in range(N):
    x, y = map(int ,input().split())
    inputList.append((x,y))

while inputList :
    x, y = inputList.pop()
    x -= 1 
    y -= 1
    badock[x][y] = 1

for i in range(0, 19, 1) :
    for j in range(0, 19, 1):
        print(badock[i][j], end=" ")
    print()