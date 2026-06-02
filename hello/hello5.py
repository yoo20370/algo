import sys 

N = int(sys.stdin.readline().rstrip())

selectMoveList = list(sys.stdin.readline().split())

distance = ['L', 'R', 'U', 'D']
distancePoint = [(0, -1), (0, 1), (-1, 0), (1, 0)]

currentX = 1
currentY = 1 

for selectMove in selectMoveList :

    for index in range(4) :
        if distance[index] == selectMove :
            currentDistanceIndex = index
            break

    moveX, moveY = distancePoint[currentDistanceIndex]

    nextX = moveX + currentX 
    nextY = moveY + currentY 

    if nextX >= 1 and nextX <= N and nextY >= 1 and nextY <= N :
        currentX = nextX
        currentY = nextY 

print(currentX, currentY)
    
