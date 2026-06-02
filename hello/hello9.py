## 왕실의 나이트 
## 이동할 수 있는 좌표 평면의 개수를 구하면 됨 
## 여기서 Map 필요한가 ?? -> 필요 없을 듯 특정 값을 벗어나면 아웃처리하면 됨 
## 이동할 수 있는 경우의 수 4가지는 저장할 필요가 있는가 ?? => 있음 그러므로 이건 모두 순회해야 하므로 List에 저장하면 될 것 같음 

import sys 

currentPosition = sys.stdin.readline().rstrip()

firstChar = currentPosition[0]
secondChar = currentPosition[1]

positionY = ord(firstChar) - ord('a') + 1
positionX = int(secondChar)

avaliableMoveCase = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

avaliableMoveCount = 0
for moveX, moveY in avaliableMoveCase :
    nextX = positionX + moveX
    nextY = positionY + moveY 

    if nextX >= 1 and nextX <= 8 and nextY >= 1 and nextY <= 8 :
        avaliableMoveCount += 1 

print(avaliableMoveCount)


