# 1차 시도 

# 현재 위치를 기준으로 왼쪽으로 갈지 오른쪽으로 갈지 결정
# 단어를 바꾸는 비용 구하고
# 이동 거리와 변경 비용을 합하면 됨 

# 2차 시도 
# 지금 문제가 뭐냐면, 가장 가까운 변경 점으로 이동하게 되면, 
# 더 먼 경우가 최소값이 경우를 놓칠 수 있음 
# 즉, 현재의 최선의 선택이 미래에 영향을 주고 있는 상태 -> 현재 접근은 잘못된 접근이므로 이를 수정해줄 필요가 있음 

# 이걸 어떻게 해결할 것인가 ?? 
# bfs를 통해서 어떤 것을 선택하는 것이 더 좋은지 전역 탐색을 해야 하는가 ?? 
## 왼쪽으로 가는 경우, 오른쪽으로 가는 경우 

# bfs로 푼다면 ??
# 왼쪽 이동, 오른쪽 이동 모두 존재  

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