# 1차 시도 

# 현재 위치를 기준으로 이동하는 거리가 
# 결국 현재 위치에서 가장 가까운 변경 점이 어딘지 확인하면 될 것 같다. 

# a b c d e f g h i j k l m n o p q r s t u v w x y z 

INF = int(1e9)

def getMinChangeCount(targetChar) :
    
    rightChangeCount = ord(targetChar) - ord('A')
    leftChangeCount = ord('Z') - ord(targetChar) + 1
    
    return min(rightChangeCount, leftChangeCount)

def getMinMoveCount(currentIndex, currentWord, targetWord) :
    
    length = len(targetWord)
    
    rightMoveIndex = currentIndex
    rightMoveCount = 0
    for moveIndex in range(length) :
        currentRightIndex = (rightMoveIndex + moveIndex) % length 
        if currentWord[currentRightIndex] != 'A' :
            rightMoveIndex = currentRightIndex
            rightMoveCount = moveIndex
            break
    else :
        return (-1, -1)
    
    leftMoveIndex = currentIndex
    leftMoveCount = 0
    for moveIndex in range(length) :
        currentLeftIndex = (leftMoveIndex - moveIndex + length) % length
        if currentWord[currentLeftIndex] != 'A' :
            
            leftMoveIndex = currentLeftIndex
            leftMoveCount = moveIndex 
            break 
    
    if leftMoveCount < rightMoveCount : 
        return (leftMoveCount, leftMoveIndex)
    else :
        return (rightMoveCount, rightMoveIndex)
    
            
def solution(name):
    
    count = 0
    
    length = len(name)
    
    currentWord = [i for i in name]
    
    currentIndex = 0 
    while "".join(currentWord) != length * 'A' :
        
        resultTuple = getMinMoveCount(currentIndex, currentWord, name) 
        moveCount, nextIndex = resultTuple

        if moveCount == -1 :
            return count
        else : 
            
            count += moveCount

            changeCount = getMinChangeCount(name[nextIndex])
            count += changeCount
            currentWord[nextIndex] = 'A'
            currentIndex = nextIndex 

    return count 