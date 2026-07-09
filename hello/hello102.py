# 2차 시도 
# 지금 문제가 뭐냐면, 가장 가까운 변경 점으로 이동하게 되면, 
# 더 먼 경우가 최소값이 경우를 놓칠 수 있음 
# 즉, 현재의 최선의 선택이 미래에 영향을 주고 있는 상태 -> 현재 접근은 잘못된 접근이므로 이를 수정해줄 필요가 있음 

# 이걸 어떻게 해결할 것인가 ?? 
# bfs를 통해서 어떤 것을 선택하는 것이 더 좋은지 전역 탐색을 해야 하는가 ?? 
## 왼쪽으로 가는 경우, 오른쪽으로 가는 경우 

# 백트래킹을 해야 하나 ?? 
# 백트래킹을 통해서 모든 경우에 대해서 구하고, 이를 바탕으로 해결하자

INF = int(1e9)

minCount = INF

def getMinChangeCount(targetChar) :
    
    rightChangeCount = ord(targetChar) - ord('A')
    leftChangeCount = ord('Z') - ord(targetChar) + 1
    
    return min(rightChangeCount, leftChangeCount)

def getLeftMoveCount(currentIndex, currentWord, targetWord) :
    
    length = len(targetWord)
    
    leftMoveIndex = currentIndex
    leftMoveCount = 0
    for moveIndex in range(length) :
        currentLeftIndex = (leftMoveIndex - moveIndex + length) % length
        if currentWord[currentLeftIndex] != 'A' :
            
            leftMoveIndex = currentLeftIndex
            leftMoveCount = moveIndex 
            return (leftMoveCount, leftMoveIndex)
            break 
            

def getRightMoveCount(currentIndex, currentWord, targetWord) :
    
    length = len(targetWord)
    
    rightMoveIndex = currentIndex
    rightMoveCount = 0
    for moveIndex in range(length) :
        currentRightIndex = (rightMoveIndex + moveIndex) % length 
        if currentWord[currentRightIndex] != 'A' :
            
            rightMoveIndex = currentRightIndex
            rightMoveCount = moveIndex
            
            return (rightMoveCount, rightMoveIndex)
            break
            

def dfs(currentIndex, currentWord, targetWord, count, length) :
    global minCount
    
    if "".join(currentWord) == length * 'A' :
        minCount = min(minCount, count)
        return
    
    # 왼쪽으로 이동한 경우 
    leftMoveCount, leftMoveIndex = getLeftMoveCount(currentIndex, currentWord, targetWord)
    if leftMoveCount == -1 :
        return
    preChar = currentWord[leftMoveIndex]  
    count += leftMoveCount
    count += getMinChangeCount(targetWord[leftMoveIndex])
    currentWord[leftMoveIndex] = 'A'
    
    dfs(leftMoveIndex, currentWord, targetWord, count, length)
    
    count -= leftMoveCount
    count -= getMinChangeCount(targetWord[leftMoveIndex])
    currentWord[leftMoveIndex] = preChar
    
    # 오른쪽으로 이동한 경우 
    rightMoveCount, rightMoveIndex = getRightMoveCount(currentIndex, currentWord, targetWord)
    preChar = currentWord[rightMoveIndex]  
    count += rightMoveCount
    count += getMinChangeCount(targetWord[rightMoveIndex])
    currentWord[rightMoveIndex] = 'A'
    
    dfs(rightMoveIndex, currentWord, targetWord, count, length)
    
    count -= rightMoveCount
    count -= getMinChangeCount(targetWord[rightMoveIndex])
    currentWord[rightMoveIndex] = preChar
        
    
def solution(name):
    global minCount

    length = len(name)
    
    currentWord = [i for i in name]
    
    dfs(0, currentWord, name, 0, length)
    
    return minCount 